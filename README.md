# MCP Writing Templates Service

This project provides a FastAPI-based service to access and manage technical writing templates for the MCP (Multi-Capability Platform) environment.

## Deployment

This service is deployed on Vercel and is connected to the `main` branch of this Git repository. Any push to the `main` branch will trigger a new deployment.

The live service is available at: [https://mcp-writing-templates.vercel.app](https://mcp-writing-templates.vercel.app)

## Registering as an MCP Tool in Trae

To make this service available as a tool within the Trae MCP marketplace, follow these steps:

1.  **Copy the Tool Definition**: The OpenAPI specification for this tool is located in the `mcp_template_tool.json` file. Copy the entire content of this file.

2.  **Navigate to the MCP Marketplace**: In the Trae user interface, go to the section for managing or adding new tools (e.g., "MCP Marketplace", "Tool Management").

3.  **Add a New Tool**: Click on the option to "Add a New Tool" or "Register a Tool".

4.  **Paste the Definition**: In the provided text area for the OpenAPI/Swagger definition, paste the content of `mcp_template_tool.json` that you copied in step 1.

5.  **Save and Publish**: Save the new tool definition. The platform will validate the specification. Once validated, you can publish the tool to make it available in the marketplace.

---