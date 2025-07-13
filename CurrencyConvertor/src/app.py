import streamlit as st
import currencies
import datetime
import humanize
from main import convert_currency , get_exchange_rate

st.title(":dollar: Currency Convertar")

st.markdown("""
This tool allows you to instantly convert amounts between different currencies 🌍.
Enter the amount and choose the currencies to see the result.
""")

currency_codes = list(currencies.MONEY_FORMATS.keys())

base_currency = st.selectbox('From Currency (Base):', currency_codes, index=currency_codes.index("USD"))
target_currency = st.selectbox('To Currency (Target):', currency_codes, index=currency_codes.index("AED"))

amount = st.number_input('Amount to Convert:', min_value=0.0, value=1.0)

if amount > 0 and base_currency and target_currency:
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    #time_diff = datetime.datetime.now() - datetime.datetime.fromtimestamp(time_last_updated)
    #time_ago = humanize.naturaltime(time_diff)

    if exchange_rate:
        converted_amount = convert_currency(amount, exchange_rate)
        st.success(f"✅ Exchange Rate: {exchange_rate:.4f}")
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Base Currency", value=f"{amount} {base_currency}")
        col2.markdown("<h1 style='color: green; text-align: center; margin: 0;'>&#8594;</h1>", unsafe_allow_html=True)
        col3.metric(label="Target Currency", value=f"{converted_amount:.2f} {target_currency}")
    else:
        st.error("Error: Unable to fetch the exchange rate. Please try again.")


st.markdown("---")
st.markdown("### ℹ️ About This Tool")
st.markdown("""
    This currency converter uses real-time exchange rates provided by the ExchangeRate-API.
    - The conversion updates automatically as you input the amount or change the currency.
    - Enjoy seamless currency conversion without the need to press a button!
    """)
