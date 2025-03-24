FROM vault.habana.ai/gaudi-docker/1.19.1/ubuntu22.04/habanalabs/pytorch-installer-2.5.1:latest

WORKDIR /workspace/

RUN git clone https://github.com/vllm-project/vllm.git /workspace/vllm \
&& cd /workspace/vllm \
&& git checkout tags/v0.7.3

WORKDIR /workspace/vllm

RUN pip install -v -r requirements-hpu.txt

ENV no_proxy=localhost,127.0.0.1
ENV PT_HPU_ENABLE_LAZY_COLLECTIVES=true

RUN VLLM_TARGET_DEVICE=hpu python3 setup.py install

RUN cd ..

