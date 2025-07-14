import asyncio 
import os 
import streamlit as st
from textwrap import dedent

from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM
from mcp_agent.workflows.llm.augmented_llm import RequestParams

st.set_page_config(page_title="Browser MCP Agent", page_icon="🌐", layout="wide")
