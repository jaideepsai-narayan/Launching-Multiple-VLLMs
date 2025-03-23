# Launching-Multiple-VLLMs
**Description:** An interactive graphical user interface (GUI) simplifies the process of deploying and interacting with Virtual Large Language Models (VLLMs). This intuitive platform provides an easy way to set up, configure, and launch VLLMs, enabling users to communicate directly with the models in a seamless chat experience.
  
**Key Features:**
- Effortless Deployment: Deploy a VLLM in just a few clicks. No need for complex configurations or technical expertise.
- Real-time Chat Interface: Engage with your VLLM in real time. Ask questions, get answers, and experiment with various queries.
- Customizable Settings: Tailor the deployment according to your needs, including model parameters, performance tuning, and more.
- Scalable Solutions: Whether you're running a small-scale model or handling large volumes of interactions, the platform can scale to meet your requirements.
- User-Friendly Interface: With a clean, accessible layout, users of all experience levels can navigate the GUI and deploy their models with ease.
- Comprehensive Feedback and Logs: Gain insights into the performance and behavior of your deployed models with detailed logs and feedback.

## Verified Environment:
[Intel® Tiber™ AI Cloud](https://www.intel.com/content/www/us/en/developer/tools/devcloud/services.html)


### Environment:
The following information outlines the specifications used for this project:

| Name      | Details                   |
|-----------|---------------------------|
| Platform  | GAUDI                     |
| Version   | 1.18.0-ee698fb            |
| OS        | Linux                     |
| Package   | pip                       |


### Environment Setup
Login to Huggingface cli, if you want to use Gated Repos

```bash
cd Launching-Multiple-VLLMs
docker build . -t vllm_gaudi2 -f Dockerfile
docker run -it -v $PWD:/workspace --runtime=habana -e HABANA_VISIBLE_DEVICES=all -e OMPI_MCA_btl_vader_single_copy_mechanism=none --cap-add=sys_nice --net=host --ipc=host vllm_gaudi2
pip install flask
cd ..
python3 new_app.py
```
![image](https://github.com/user-attachments/assets/59aeb052-1f47-470c-b938-0cde71cdff3b)







