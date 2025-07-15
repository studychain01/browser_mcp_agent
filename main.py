import asyncio 
import os 
import streamlit as st
from textwrap import dedent

from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM
from mcp_agent.workflows.llm.augmented_llm import RequestParams

st.set_page_config(page_title="Browser MCP Agent", page_icon="🌐", layout="wide")

st.markdown("<h1 class='main-header'> Browser MCP Agent </h1>", unsafe_allow_html=True)
st.markdown("Interact with a powerful web browsing agent that can navigate and interact with websites")


with st.sidebar:

    if not os.getenv("OPENAI_API_KEY"):
        api_key = st.text_input("OpenAI API Key:", type="password")

        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key


    st.markdown("## Example Commands")

    st.markdown("**Navigation**")
    st.markdown("- Go to wikipedia.org/wiki/computer_vision")

    st.markdown("**Interactions**")
    st.markdown("- Click on the link to object detection and take a screenshot")
    st.markdown("- Scroll down to view more content")

    st.markdown("**Multi-step Tasks**")
    st.markdown("- Navigate to wikipedia.org/wiki/computer_vision, scroll down, and report details")
    st.markdown("- Scroll down and summarize the wikipedia page")
    
    st.markdown("---")
    st.caption("Note: The agent that uses Puppeteer to control a real browser.")

query = st.text_area("Your Command", placeholder="Ask the agent to navigate to websites and interact with them")

#Initialize the agent
if 'intialized' not in st.session_state:
    st.session_state.intialized = False
    st.session_state.mcp_app = MCPApp(name="streamlit_mcp_agent")
    st.session_state.mcp_context=None
    st.session_state.mcp_agent_app=None
    st.session_state.browser_agent=None 
    st.session_state.llm = None

    #loop helps turn sync code into async
    st.session_state.loop = asyncio.new_event_loop()
    asyncio.set_event_loop(st.session_state.loop)

async def setup_agent():
    if not st.session_state.intialized:
        try: 
           st.session_state.mcp_context = st.session_state.mcp_app.run()
           st.session_state.mcp_agent_app = await st.session_state.mcp_context.__aenter__()

           st.session_state.browser_agent = Agent(
              name="browser",
              instruction="""You are a helpful web browsing assistant that can interact with websites using puppeteer. 
                  - Navigate to websites and perform browser actions (click, scroll, type)
                  - Extract information from web pages
                  - Take screenshots of page elements when useful
                  - provide concise summaries of web content using markdown
                  - Follow multi-step browsing sequences to complete tasks

                  when navigating, start with "www.lastmileai.dev" unless instructed otherwise.""",
               server_names=["puppeteer"],
           )

           await st.session_state.browser_agent.initialize()
           st.session_state.llm = await st.session_state.browser_agent.attach_llm(OpenAIAugmentedLLM)

           logger = st.session_state.mcp_agent_app.logger
           tools = await st.session_state.browser_agent.list_tools()
           logger.info("Tools Available:", data=tools)

           st.session_state.intialized = True
        
        except Exception as e:
            return f"Error during intialization: {str(e)}"
    
    return None 

async def run_mcp_agent(message):
    if not os.getenv("OPENAI_API_KEY"):
        return "Error: OPENAI_API_KEY is not set in the environment variables"
    
    try:
        error = await setup_agent()
        if error: 
            return error
        
        result = await st.session_state.llm.generate_str(
            message=message,
            request_params=RequestParams(use_history=True)
        )
        return result 
    except Exception as e: 
        return f"Error: {str(e)}"

if st.button("Run Command", type="primary", use_container_width=True):
    with st.spinner("Processing your request..."):
        result = st.session_state.loop.run_until_complete(run_mcp_agent(query))

        st.markdown("### Response")
        st.markdown(result)

#locals()	Returns a dictionary of variables local to the current function or block
if 'result' not in locals():
    st.markdown(
        """<div style='padding: 20px; background-color: #f0f2f6; border-radius: 10px;'>
        <h4>How to use this app:</h4>
        <ol>
            <li>Enter your OpenAI API key in your mcp_agent.secrets.yaml file</li>
            <li>Type a command for the agent to navigate and interact with websites</li>
            <li>Click 'Run Command' to see results</li>
        </ol>
        <p><strong>Capabilities:</strong></p>
        <ul>
            <li>Navigate to websites using Puppeteer</li>
            <li>Click on elements, scroll, and type text</li>
            <li>Take screenshots of specific elements</li>
            <li>Extract information from web pages</li>
            <li>Perform multi-step browsing tasks</li>
        </ul>
        </div>""", 
        unsafe_allow_html=True
    )

# Footer
st.markdown("---")
st.write("Built with Streamlit, Puppeteer, and MCP-Agent Framework ❤️")

