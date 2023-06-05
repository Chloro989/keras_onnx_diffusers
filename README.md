# keras_onnx_diffusers

This repository is for those who want try keras_cv or onnx diffusers.

このレポジトリはkeras_cvやonnxを使用したい人を対象としています。

---

Keras_cv provides a unique and fast diffuser.([URL](https://keras.io/keras_cv/))

Also check out this:[High-performance image generation using Stable Diffusion in KerasCV](https://keras.io/guides/keras_cv/generate_images_with_stable_diffusion/)

keras_cvのdiffuserは速いのが特徴です。([リンク](https://keras.io/keras_cv/))

こちらもチェックして下さい:[High-performance image generation using Stable Diffusion in KerasCV](https://keras.io/guides/keras_cv/generate_images_with_stable_diffusion/)

---

Onnx runtime supports various GPU software and APIs.
Thus, you can run diffusers on Windows-AMD environment.

onnxは多くのGPUソフトウェアやAPIをサポートしています。
そのため、Windows-AMD環境でもdiffuserを使用することが出来ます。

---

# Installation

1.Run the code below

```bash
curl -sSL https://raw.githubusercontent.com/Chloro989/keras_onnx_diffusers/main/install.sh | bash

```
# Simple troubleshooting

Windows: Installing Windows Subsystem for Linux (WSL) or Git Bash

Windows users can use either Windows Subsystem for Linux (WSL) or Git Bash to run the curl command.

Windows Subsystem for Linux (WSL): WSL allows you to run a Linux environment directly on Windows, without the overhead of a traditional virtual machine. You can follow the official Microsoft guide to install WSL: [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install)

Git Bash: Git Bash is an application that provides Git command line features on Windows. It's a part of Git for Windows and provides a BASH emulation used to run Git from the command line. You can download it from the official Git for Windows website: [Git for Windows](https://gitforwindows.org/)

macOS/Linux: On macOS and Linux, curl and bash are usually installed by default. If not, you can install them using the package manager for your system (brew for macOS, apt for many Linux distributions).

Troubleshooting:

    Windows: Install Windows Subsystem for Linux (WSL) or Git Bash.
    macOS/Linux: If curl or bash is not installed, you can install them using the package manager for your system (brew for macOS, apt for many Linux distributions).
    
---

Windows: Windows Subsystem for Linux (WSL) または Git Bash のインストール

Windowsユーザーは、Windows Subsystem for Linux (WSL) または Git Bash を使用してコマンドを実行できます。

Windows Subsystem for Linux (WSL): WSLは、従来の仮想マシンのオーバーヘッドなしに、直接Windows上でLinux環境を実行することを可能にします。公式のMicrosoftガイドに従ってWSLをインストールすることができます：[WSLのインストール](https://learn.microsoft.com/en-us/windows/wsl/install)

Git Bash: Git Bashは、Windows上でGitコマンドライン機能を提供するアプリケーションです。Git for Windowsの一部であり、コマンドラインからGitを実行するために使用されるBASHエミュレーションを提供します。公式のGit for Windowsウェブサイトからダウンロードすることができます：[Git for Windows](https://gitforwindows.org/)

macOS/Linux: macOSとLinuxでは、通常curlとbashはデフォルトでインストールされています。もしインストールされていない場合は、システムのパッケージマネージャー（macOSではbrew、多くのLinuxディストリビューションではapt）を使用してインストールできます。

トラブルシューティング：

    Windows: Windows Subsystem for Linux (WSL) または Git Bash をインストールします。
    macOS/Linux: curlやbashがインストールされていない場合、システムのパッケージマネージャー（macOSではbrew、多くのLinuxディストリビューションではapt）を使用してインストールします。
