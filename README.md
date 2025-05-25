![Header](https://github.com/k4itrun/erisphisher/assets/103044629/427fe022-c889-4e09-8075-a9e7f89cf08c)

<div align="center">
  <a aria-label="GitHub Maintained" href="https://github.com/k4itrun/erisphisher/blob/master/license.md">
    <img src="https://img.shields.io/badge/No-yellow?logo=github&style=flat-square&label=Maintained%3F">
  </a>
  <a aria-label="License" href="https://github.com/k4itrun/erisphisher/blob/master/license.md">
    <img src="https://img.shields.io/github/license/k4itrun/erisphisher?color=yellow&logo=github&style=flat-square&label=License">
  </a>
  <a aria-label="Version" href="https://github.com/k4itrun/erisphisher/releases">
    <img src="https://img.shields.io/github/v/release/k4itrun/erisphisher?color=yellow&logo=github&style=flat-square&label=Version">
  </a>
  <a aria-label="Discord" href="https://discord.gg/A6Vu7gYE">
    <img src="https://img.shields.io/discord/903684797560397915?color=yellow&logo=discord&style=flat-square&logoColor=fff&label=Discord">
  </a>
</div>

<div align="center">
  <a aria-label="Stars" href="https://github.com/k4itrun/erisphisher">
    <img src="https://img.shields.io/github/stars/k4itrun/erisphisher?color=yellow&logo=github&style=flat-square&label=Stars">
  </a>
  <a aria-label="Forks" href="https://github.com/k4itrun/erisphisher/releases">
    <img src="https://img.shields.io/github/forks/k4itrun/erisphisher?color=yellow&logo=github&style=flat-square&label=Forks">
  </a>
  <a aria-label="Issues" href="https://github.com/k4itrun/erisphisher/issues">
    <img src="https://img.shields.io/github/issues/k4itrun/erisphisher?color=yellow&logo=github&style=flat-square&label=Issues">
  </a>
</div>

---

## Table of Contents

1. [Overview](#overview)
   - [Notable Features](#notable-features)
2. [Getting Started](#getting-started)
   - [System Requirements](#system-requirements)
   - [Platform Support](#platform-support)
   - [Installing packages](#installing-packages)
   - [Installation](#installation)
3. [Usage](#usage)
4. [Acknowledgments](#acknowledgments)
5. [Contributing](#contributing)
6. [Contact](#contact)
7. [License](#license)
8. [Disclaimer](#disclaimer)

## Overview

Eris is a user-friendly tool designed to streamline phishing simulation campaigns by providing access to over 60 customizable templates. Whether you're conducting red team assessments, training employees on cybersecurity awareness, or testing your organization’s email defenses, Eris empowers you with the tools to create realistic, high-impact scenarios in minutes.

### Notable Features

- **Multi-Platform Support:** Compatible with most Linux distributions.
- **Over 60 Website Templates:** Choose from a wide variety of templates for your projects.
- **Dual Tunneling Options:** Utilize both Ngrok and Cloudflared for tunneling.
- **User-Friendly Interface:** Designed for ease of use, making it accessible for all skill levels.
- **Error Diagnostic Capabilities:** Built-in features for identifying and resolving issues.
- **URL Masking:** Mask URLs for added security.
- **Custom URL Masking:** Tailor URL masking to your specific needs.
- **Portability:** Run from any directory; no installation required.
- **Retrieve IP Addresses and More:** Access detailed information, including login credentials.

## Getting Started

### System Requirements

To run this application smoothly, ensure that you have the following prerequisites in place:

- `python3` Runs the script
- `php` Backend support
- `curl` Network requests
- `wget` Downloads files
- `unzip` Extracts ZIPs
- `~100MB` Disk space (minimum)

> [!NOTE]
> During the initial run, the system will take care of the complete installation of all necessary dependencies without any manual intervention required on your part

### Platform Support

| OS      | Support Level                                              |
| ------- | ---------------------------------------------------------- |
| Windows | Unsupported (Consider using Docker, VirtualBox, or VMware) |
| iPhone  | Alpha (Docker recommended)                                 |
| MacOS   | Alpha (Docker recommended)                                 |
| Linux   | Excellent                                                  |
| Android | Excellent                                                  |

### Installing packages

- For Termux

```bash
pkg install git python3 python-pip php openssh -y
```

- For Debian (Debian, Ubuntu, Kali, Parrot)

```bash
sudo apt install git python3 python3-pip php openssh-client -y
```

- For Redhat (Fedora)

```bash
sudo dnf install git python3 php openssh -y
```

- For Arch (Manjaro)

```bash
sudo pacman -S git python3 python-pip php openssh --noconfirm
```

### Installation

#### Use Google Shell to test this online tool

<p align="left">
  <a href="https://shell.cloud.google.com/cloudshell/open?cloudshell_git_repo=https://github.com/k4itrun/erisphisher.git&tutorial=README.md" target="_blank"><img src="https://gstatic.com/cloudssh/images/open-btn.svg"></a>
</p>

To ensure **erisphisher** runs smoothly, please do the following:

```bash
git clone https://github.com/k4itrun/erisphisher.git
```

```bash
cd erisphisher
```

```bash
bash eris.sh
```

- For Termux

```bash
pkg install tur-repo
```

```bash
pkg install erisphisher
```

```bash
erisphisher
```

> [!NOTE]
> Termux strongly discourages any hacking-related discussions. Therefore, please refrain from discussing any topics related to **erisphisher** in any of the Termux discussion groups. For more information, refer to the: [wiki](https://wiki.termux.com/wiki/hacking)

- Or, directly run

```bash
git clone https://github.com/k4itrun/erisphisher && cd erisphisher && bash eris.sh
```

## Usage

## Acknowledgments

This project is inspired by several phishing tools. Special thanks to:

- [htr-tech](https://github.com/htr-tech/zphisher/blob/master/zphisher.sh#L204): Some templates and base codes were taken from [zphisher](https://github.com/htr-tech/zphisher/blob/master/zphisher.sh#L204)

> [!WARNING]
> I am not currently supporting this project in recommended updates, in the future maybe yes, for now you will have this minimalist version.

## Contributing

### Reporting Issues

If you encounter any bugs or problems while using the tool, please open a [new Issue here](https://github.com/k4itrun/erisphisher/issues).
To help us assist you faster, include as much detail as possible, such as:

- What you were trying to do.
- Any error messages or console logs.
- Your environment details (OS, versions, etc.)

The more info you provide, the quicker we can identify and fix the problem.

### Pull Requests

Thanks for wanting to contribute! To submit improvements or fixes, please follow these steps:

1. Clone [this repository](https://github.com/k4itrun/erisphisher.git) using `git clone https://github.com/k4itrun/erisphisher.git`.
2. Create a new branch from `main` with a clear, descriptive name, for example: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them with clear, meaningful messages.
4. Open a [new Pull Request here](https://github.com/k4itrun/erisphisher/pulls), explaining what you added or fixed and why.

We’ll carefully review each PR and provide feedback if needed to help you get it merged.

☕ **[Thank you for your support!](https://ko-fi.com/A0A11481X5)**

## Contact

If you have any **Questions** or need **Help**, feel free to email me at <tsx@billoneta.xyz> or join the **[Discord server](https://discord.gg/CMNd45AXvD)**.

## License

This project is released under the **[MIT License](license.md)**. See LICENSE file for more info.

## Disclaimer

### Important Notice: Educational Use Only.

This tool is designed solely for educational purposes. Any misuse of this tool is strictly prohibited. By using this tool, you acknowledge and accept these terms.

### User Accountability:

By utilizing this tool, you take full responsibility for your actions. The creator disclaims any liability for misuse. It is your responsibility to ensure that your use of this software complies with all applicable laws and regulations.

### No Assistance:

The creator will not provide assistance or support for any misuse of this tool. Any inquiries related to harmful or illegal activities will be ignored.

### Terms Acceptance:

By using this tool, you agree to abide by this disclaimer. If you do not agree with these terms, please do not use the software.

<details>
 <summary>You didn’t break it. It was waiting to break. 🎁</summary>

<a href="https://star-history.com/#k4itrun/erisphisher&Timeline">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=k4itrun/erisphisher&type=Timeline&theme=dark" />
    <img alt="Star History Erisphisher" src="https://api.star-history.com/svg?repos=k4itrun/erisphisher&type=Timeline" />
  </picture>
</a>

</details>
