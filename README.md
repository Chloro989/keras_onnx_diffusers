# keras_onnx_diffusers

This repository is for those who want try ~~keras_cv~~ or onnx diffusers.

このレポジトリは~~keras_cv~~やonnxを使用したい人を対象としています。

---


Keras_cv provides a unique and fast diffuser.([link](https://keras.io/keras_cv/))

Also check out this:[High-performance image generation using Stable Diffusion in KerasCV](https://keras.io/guides/keras_cv/generate_images_with_stable_diffusion/)

keras_cvのdiffuserは速いのが特徴です。([リンク](https://keras.io/keras_cv/))

こちらもチェックして下さい:[High-performance image generation using Stable Diffusion in KerasCV](https://keras.io/guides/keras_cv/generate_images_with_stable_diffusion/)

---

Onnx runtime supports various GPU software and APIs.
**Thus, you can run diffusers on Windows-AMD environment.[link](https://onnxruntime.ai/)**

onnxは多くのGPUソフトウェアやAPIをサポートしています。
**そのため、Windows-AMD環境でもdiffuserを使用することが出来ます。[リンク](https://onnxruntime.ai/)**

---

# Local Installation(English)

## **Impotant messages here**

### **⚠️Don't Skip a Step!⚠️**

### **As of 2023/06/06, This Repo Only Suppots Windows Users.**

## 1.Install poetry and pyenv

[How to install poetry](https://python-poetry.org/docs/#installation)

[How to install pyenv](https://github.com/pyenv/pyenv#installation)

## 2.Open shell(terminal,command prompt..). Copy and paste and run the following code.

### From PowerShell

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Chloro989/keras_onnx_diffusers/master/install.sh" -OutFile "install.ps1"
powershell ./install.ps1

```
If this won't work, check the trouble shooting.
If you already have gitbash, you may run the code below in gitbash.

### From Linux/Mac/GitBash Shell 

```bash
curl -sSL https://raw.githubusercontent.com/Chloro989/keras_onnx_diffusers/master/install.sh | bash
```

### Other

Or make a folder named `keras_onnx_diffusers` on desktop.
And in `keras_onnx_diffusers`, run `git clone https://github.com/Chloro989/keras_onnx_diffusers.git`.

## Making a environment and Installing Packages.

```bash
cd "~/Desktop/keras_onnx_diffusers"
pyenv install 3.10.6
pyenv local 3.10.6
python -m pip install --upgrade pip
poetry install
```

## Installing a Model

```bash
cd "~/Desktop/keras_onnx_diffusers"
git clone https://huggingface.co/runwayml/stable-diffusion-v1-5 --branch onnx --single-branch model/stable_diffusion_onnx
```
## Installing ORT-Nightly

### 1. Go to this page:[link](https://aiinfra.visualstudio.com/PublicPackages/_artifacts/feed/ORT-Nightly/PyPI/ort-nightly-directml/overview/1.16.0.dev20230601002)

### 2. Download GPU Support

#### Windows

![image](https://github.com/Chloro989/keras_onnx_diffusers/assets/84625053/3c50d55e-92ce-4acf-b289-06ec715f7542)

#### Linux/Mac

🚧I don't know🚧

### 3. Open PowerShell/CommandPrompt e.t.c and run command

(The code is not copy and patseable, you need to change it by yourself)

```bash
cd "~/Desktop/keras_onnx_diffusers"
poetry run pip install "C:\your\path\to\ort_nightly_directml-X.XX.X.devSOMEKINDOFDATE-cp310-cp310-win_amd64.whl" --force-reinstall
```

For example, in my case, I download "ort_nightly_directml-1.16.0.dev20230601002-cp310-cp310-win_amd64.whl" in "C:\Users\Chloro989\Downloads' . So I will run 

```bash
cd "~/Desktop/keras_onnx_diffusers"
poetry run pip install "C:\Users\Chloro989\Downloads\ort_nightly_directml-1.16.0.dev20230601002-cp310-cp310-win_amd64.whl" --force-reinstall
```

in my powershell.

# Execution

Run this code.

```bash
cd "~/Desktop/keras_onnx_diffusers"
poetry run python onnx_diffusion.py
```
If you wish, you can run from jupyter lab(There is a ipynb file).
(Don't forget to create a kernel for the environment you made.)

# Simple Troubleshooting

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
