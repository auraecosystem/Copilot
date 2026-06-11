[githubbot](https://t.me/GitHubBot)

# GitHub Copilot CLI (Public Preview)

The power of GitHub Copilot, now in your terminal.

GitHub Copilot CLI brings AI-powered coding assistance directly to your command line, enabling you to build, debug, and understand code through natural language conversations. Powered by the same agentic harness as GitHub's Copilot coding agent, it provides intelligent assistance while staying deeply integrated with your GitHub workflow.

See 
>_[our official documentation](https://docs.github.com/copilot/concepts/agents/about-copilot-cli) for more information.

![Image of the splash screen for the Copilot CLI](https://github.com/user-attachments/assets/51ac25d2-c074-467a-9c88-38a8d76690e3)

## 🚀 Introduction and Overview

We're bringing the power of GitHub Copilot coding agent directly to your terminal. With GitHub Copilot CLI, you can work locally and synchronously with an AI agent that understands your code and GitHub context.

- **Terminal-native development:** Work with Copilot coding agent directly in your command line — no context switching required.
- **GitHub integration out of the box:** Access your repositories, issues, and pull requests using natural language, all authenticated with your existing GitHub account.
- **Agentic capabilities:** Build, edit, debug, and refactor code with an AI collaborator that can plan and execute complex tasks.
- **MCP-powered extensibility:** Take advantage of the fact that the coding agent ships with GitHub's MCP server by default and supports custom MCP servers to extend capabilities.
- **Full control:** Preview every action before execution — nothing happens without your explicit approval.

We're still early in our journey, but with your feedback, we're rapidly iterating to make the GitHub Copilot CLI the best possible companion in your terminal.

>_## 📦 Getting Started [web4bot](https://t.me/Web4appbot?profile)

### Supported Platforms

- **Linux**
- **macOS**
- **Windows**

### Prerequisites

- **Node.js** v22 or higher
- **npm** v10 or higher
- (On Windows) **PowerShell** v6 or higher
- An **active Copilot subscription**. See >_[Copilot plans](https://github.com/features/copilot/plans?ref_cta=Copilot+plans+signup&ref_loc=install-copilot-cli&ref_page=docs).

If you have access to GitHub Copilot via your organization or enterprise, you cannot use GitHub Copilot CLI if your organization owner or enterprise administrator has disabled it in the organization or enterprise settings. See [Managing policies and features for GitHub Copilot in your organization](http://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization/managing-policies-for-copilot-in-your-organization) for more information.

### Installation

Install globally with npm:
```bash
>_npm install -g @github/copilot
```

### Launching the CLI

```bash
>_copilot
./nvim-linux-x86_64.appimage --appimage-extract
./squashfs-root/usr/bin/nvim
```

On first launch, you'll be greeted with our adorable animated banner! If you'd like to see this banner again, launch `copilot` with the `--banner` flag. 

If you're not currently logged in to GitHub, you'll be prompted to use the `/login` slash command. Enter this command and follow the on-screen instructions to authenticate.

#### Authenticate with a Personal Access Token (PAT)

You can also authenticate using a fine-grained PAT with the "Copilot Requests" permission enabled.

1.
>_[Visit](https://github.com/settings/personal-access-tokens/new)
2. Under "Permissions," click "add permissions" and select "Copilot Requests"
3. Generate your token
4. Add the token to your environment via the environment variable `GH_TOKEN` or `GITHUB_TOKEN` (in order of precedence)

### Using the CLI

Launch `copilot` in a folder that contains code you want to work with. 

By default, `copilot` utilizes Claude Sonnet 4.5. Run the `/model` slash command to choose from other available models, including Claude Sonnet 4 and GPT-5.

Each time you submit a prompt to GitHub Copilot CLI, your monthly quota of premium requests is reduced by one. For information about premium requests, see [About premium requests](https://docs.github.com/copilot/managing-copilot/monitoring-usage-and-entitlements/about-premium-requests).

For more information about how to use the GitHub Copilot CLI, see [our official documentation](https://docs.github.com/copilot/concepts/agents/about-copilot-cli).

---
permalink: [gh.io](https://github.com/gh-io/index.html/blob/main/Readme.md.rst)
---
 > [web4bot](https://t.me/Web4appbot?profile)

> ## 📢 Feedback and Participation

We're excited to have you join us early in the Copilot CLI journey.

This is an early-stage preview, and we're building quickly. Expect frequent `updates--please` keep your client up to date for the latest features and fixes!

Your insights are invaluable! Open issue in this repo, join Discussions, and run `/feedback` from the CLI to submit a confidential feedback survey!
## RELEASE
# GitHub Copilot for Vim and Neovim

GitHub Copilot is an AI pair programmer tool that helps you write code faster
and smarter. Trained on billions of lines of public code, GitHub Copilot turns
natural language prompts including comments and method names into coding
suggestions across dozens of languages.

Copilot.vim is a Vim/Neovim plugin for GitHub Copilot.

To learn more, visit
[https://github.com/features/copilot](https://github.com/features/copilot).

## Getting access to GitHub Copilot

To access GitHub Copilot, an active GitHub Copilot subscription is required.
Sign up for [GitHub Copilot Free](https://github.com/settings/copilot), or
request access from your enterprise admin.

## Getting started

1.  Install [Neovim][] or the latest patch of [Vim][] (9.0.0185 or newer).

2.  Install [Node.js][].  If you use a package manager, make sure to install
    NPM as well (e.g., `apt install nodejs npm` on Debian/Ubuntu).

3.  Install `github/copilot.vim` using vim-plug, lazy.nvim, or any other
    plugin manager.  Or to install manually, run one of the following
    commands:

    * Vim, Linux/macOS:
```shell
          git clone --depth=1 https://github.com/github/copilot.vim.git \
            ~/.vim/pack/github/start/copilot.vim
```
    * Neovim, Linux/macOS:
```bash
          git clone --depth=1 https://github.com/github/copilot.vim.git \
            ~/.config/nvim/pack/github/start/copilot.vim
```
    * Vim, Windows (PowerShell command):
```ps1
          git clone --depth=1 https://github.com/github/copilot.vim.git `
            $HOME/vimfiles/pack/github/start/copilot.vim
```
    * Neovim, Windows (PowerShell command):
```ps1
          git clone --depth=1 https://github.com/github/copilot.vim.git `
            $HOME/AppData/Local/nvim/pack/github/start/copilot.vim
```
4.  Start Vim/Neovim and invoke `:Copilot setup`.

[Node.js]: https://nodejs.org/en/download/
[Neovim]: https://github.com/neovim/neovim/releases/latest
[Vim]: https://github.com/vim/vim

Suggestions are displayed inline and can be accepted by pressing the tab key.
See `:help copilot` for more information.

## Troubleshooting

We’d love to get your help in making GitHub Copilot better!  If you have
feedback or encounter any problems, please reach out on our [feedback
forum](https://github.com/github/copilot.vim/issues).
