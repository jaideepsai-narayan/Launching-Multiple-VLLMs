# Launching-Multiple-VLLMs
- **Description:** Our interactive graphical user interface (GUI) simplifies the process of deploying and interacting with Virtual Large Language Models (VLLMs). This intuitive platform provides an easy way to set up, configure, and launch VLLMs, enabling users to communicate directly with the models in a seamless chat experience.
  
Key Features:
- Effortless Deployment: Deploy a VLLM in just a few clicks. No need for complex configurations or technical expertise.
- Real-time Chat Interface: Engage with your VLLM in real time. Ask questions, get answers, and experiment with various queries.
- Customizable Settings: Tailor the deployment according to your needs, including model parameters, performance tuning, and more.
- Scalable Solutions: Whether you're running a small-scale model or handling large volumes of interactions, the platform can scale to meet your requirements.
- User-Friendly Interface: With a clean, accessible layout, users of all experience levels can navigate the GUI and deploy their models with ease.
- Comprehensive Feedback and Logs: Gain insights into the performance and behavior of your deployed models with detailed logs and feedback.

## Verified Environment:
[Intel® Tiber™ AI Cloud](https://www.intel.com/content/www/us/en/developer/tools/devcloud/services.html)


### Environment Setup:
The following information outlines the specifications used for this project:

| Name      | Details                   |
|-----------|---------------------------|
| Platform  | GAUDI                     |
| Version   | 1.18.0-ee698fb            |
| OS        | Linux                     |
| Package   | pip                       |


### Environment Setup

```bash
python3 -m venv vllama
source vllama/bin/activate
python -m ipykernel install --user --name vllama
```


Install the packages with help of requirements.txt file:

```
cd video-analytics
pip install -r requirements.txt
```
```
pip install --upgrade --upgrade-strategy eager "optimum[neural-compressor]"
```
Install [IPEX](https://intel.github.io/intel-extension-for-pytorch/index.html#installation?platform=gpu&version=v2.1.30%2bxpu&os=linux%2fwsl2&package=pip) with the below commands:
```
python -m pip install torch==2.1.0.post3 torchvision==0.16.0.post3 torchaudio==2.1.0.post3 intel-extension-for-pytorch==2.1.40+xpu oneccl_bind_pt==2.1.400+xpu --extra-index-url https://pytorch-extension.intel.com/release-whl/stable/xpu/us/
```
```
python -m pip install numpy==1.26.4
```

## Acknowledgement:
We are grateful for the incredible projects that our [video_analytics](https://github.com/rskasturi/usecases/edit/master/video_analytics) has emerged from:

[Video-LLAMA](https://github.com/DAMO-NLP-SG/Video-LLaMA) is the core of this project, where we successfully ran it on both CPUs and XPUs.

[LLAMA](https://github.com/meta-llama/llama) Open and Efficient Foundation Language Models.

[LLaVA](https://github.com/haotian-liu/LLaVA) Large Language and Vision Assistant








