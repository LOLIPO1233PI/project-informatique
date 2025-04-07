import file_handler
import html_miscs
import pandas
import os
import streamlit as st

print("\033[2J\033[3J\033[HStarting ...")


st.set_page_config(
    "YesPing Presentation", page_icon=os.path.join("images", "favicon.ico")
)
st.markdown(file_handler.load_css("default"), unsafe_allow_html=True)
st.markdown(file_handler.html_handler("logo"), unsafe_allow_html=True)
st.markdown(
    html_miscs.center_text("Everyone has the right to experience good internet", 27),
    unsafe_allow_html=True,
)

st.markdown("---")
st.subheader("What we will talk about:")
st.markdown("↪ What we provide for our clients")
st.markdown("↪ What we will choose for your network installation")
st.markdown("↪ What will be the price of the installation")
st.markdown("---")
tab1, tab2, tab3 = st.tabs(
    [
        "What we will offer you",
        "What we will choose for your network installation",
        "Price of the installation",
    ]
)


def part1() -> None:
    st.markdown(
        "↪ :blue-background[Extremely fast internet speeds with the help of our sponsor :orange[Orange]]"
    )
    st.markdown("↪ :green-background[Protection against DDOS attacks]")
    st.markdown(
        "↪ :red-background[Adapted network infrastructure suited for your needs]"
    )
    st.markdown("↪ :orange-background[Quality materials]")


def part2() -> None:
    st.markdown(file_handler.txtfile_handler("netchoice"))

def part3() -> None:
    data = pandas.read_excel(os.path.join("data", "materials.xlsx"))
    total_price = [list(data["Quantity"]), list(data["Unit Price (USD)"])]
    prices = []
    for i in range(len(total_price[0])):
        prices.append(total_price[0][i] * total_price[1][i])
    prices = f"{sum(prices)} $"
    st.table(data)
    st.metric("Total Price USD:", prices, border=True)


with tab1:
    part1()
with tab2:
    part2()
with tab3:
    part3()
