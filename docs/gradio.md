TODO:
1. 为什么（只是其中一个框架而已）
2. 迅速入门（slot的输入和输出分别有两种模式），常用的Interface
3. （可能需要结合一下html、css的概？比如盒模型）
4. 自定义的gr.Block
5. 自定义css


Gradio Block is AWESOME
in order to update component, need to return value from func
as for State, input and output are needed at the same time
as for common variable, use global is just fine


https://www.gradio.app/guides


方便起见，不携带数据的请求使用get，携带数据的请求使用post
inference endpoint


modified README.md
make it hf-like


weird things

with gr.Row(visible=False) as canvas:
    with gr.Row(elem_id) as container:
        pass
这样才能不见，不然的话，可能是因为css的原因导致visible不生效


---