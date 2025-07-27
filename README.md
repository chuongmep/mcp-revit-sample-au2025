# mcp-revit-sample-au2025

Demo sample MCP integration with revit data at AU 2025


## System requirements

- Python 3.10 or higher installed.
- You must use the Python MCP SDK 1.2.0 or higher.
- The demo using Github Copilot Chat in Vscode, so you need to install the [Github Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) and [Vscode](https://code.visualstudio.com/) to run the demo. Some subscription may be required for the Copilot Chat.

## Set up your environment
First, let’s install uv and set up our Python project and environment:

Macos/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Windows:
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Set up your project

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mcp-revit-sample-au2025.git
cd mcp-revit-sample-au2025
```
2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required packages:

```bash
# Install dependencies
uv add mcp[cli] httpx
```
4. configuration file (Use Claude):

Macos/Linux:
```bash
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```
Windows:
```bash
code $env:AppData\Claude\claude_desktop_config.json
```

Paste the following configuration into the file:

```json
{
  "mcpServers": {
    "revit-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/your/mcp-revit-sample-au2025",
        "run",
        "revit.py"
      ]
    }
  }
}
```

Config using VsCode : 

1. Create a `.vscode` folder in the root of your project.
2. Create a `mcp.json` file inside the `.vscode` folder.
3. Paste the following configuration into the `mcp.json` file:

```json
{
  "servers": {
    "revit-mcp-vscode": {
      "command": "uv",
      "type": "stdio",
      "args": [
        "--directory",
        "C:\\Users\\chuon\\Downloads\\repos\\mcp-revit-sample-au2025",
        "run",
        "revit.py"
      ],
      "env": {

      }
    }
  }
}
```
4. Restart Vscode. 
5. Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P) and type "MCP: Start Server" to start the MCP server.

## Preview

![preview](./docs/iShot_2025-07-27_14.09.15.png)


## Knowledge

- [Quick Start with MCP SDK](https://modelcontextprotocol.io/quickstart/server/)
- [MCP SDK Documentation](https://modelcontextprotocol.io/docs/sdk/)