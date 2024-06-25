import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")


