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