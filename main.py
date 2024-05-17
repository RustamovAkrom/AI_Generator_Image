import replicate
import streamlit as st
from modules import SDXL, STABLELM_BASE_ALPHA_3D, STABLE_DUFFUSION

st.markdown("# :raindow[AI Generate Image]")

REPLICATE_API_TOKEN = st.secrets['REPLICATE_API_TOKEN']

def configure_sidebar():
    with st.sidebar:
        with st.form("my_form"):
            width = st.number_input("Width", min_value=256, max_value=1024, value=1024, step=16)
            height = st.number_input("Height", min_value=256, max_value=1024, value=1024, step=16)
            prompt = st.text_area("Prompt")
            submit = st.form_submit_button("Submit", type="primary")

        return {
            "width": width,
            "height": height,
            "prompt": prompt,
            "submit": submit
        }
    

def main_page(
    width: int,
    height: int,
    prompt: str,
    submit: bool
):  
    if submit:
        with st.spinner("Generating..."):
            result = replicate.run(
                ref = SDXL,
                input = {
                    "width": width,
                    "height": height,
                    "prompt": prompt,
                    "scheduler": "K_EULER",
                    "num_outputs": 1,
                    "guidance_scale": 7.5,
                    "num_inference_steps": 50
                    })
            image = result[0]

            with st.container():
                st.image(image, caption="Your generating image")


def main():
    data = configure_sidebar()
    main_page(**data)

if __name__=="__main__":
    main()