# mcp-revit-sample-au2025
demo sample integration with revit at AU 2025


Command Modify in macos 

```bash
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```


## Server configuration

```bash
{
  "mcpServers": {
    "revit-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/chuong/Documents/github/mcp-revit-sample-au2025",
        "run",
        "revit.py"
      ]
    }
  }
}
```