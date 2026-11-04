import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from data_loader import fetch_price_data
from metrics import value_at_risk_historical, value_at_risk_parametrical, portfolio_var_historical, portfolio_var_parametrical, expected_shortfall, sharpe_ratio, MDD
from visualization import kde_plot

st.title("📊 Risk Analytics Dashboard")

st.sidebar.header("Ustawienia")
ticker_list = st.sidebar.text_input("Tickery (po przecinku)", "AAPL, MSFT, GOOGL")
confidence = st.sidebar.slider("Poziom ufności VaR", 0.90, 0.99, 0.95, 0.01)
weights_input = st.sidebar.text_input("Wagi spółek (po przecinku)", "")

tickers = [t.strip().upper() for t in ticker_list.split(",") if t.strip()]

if tickers:
    prices = fetch_price_data(tickers, start_date="2023-01-01", end_date="2026-01-01")
    returns = prices.pct_change().dropna()

    n = len(tickers)
    if weights_input:
        try:
            weights = np.array([float(w.strip()) for w in weights_input.split(",")])
            weights = weights / weights.sum()
        except ValueError:
            st.warning("Niepoprawny format wag. Zastosowano równe wagi.")
            weights = np.ones(n) / n
    else:
        weights = np.ones(n) / n

    port_var_hist = portfolio_var_historical(returns, confidence, weights)
    port_var_param = portfolio_var_parametrical(returns, confidence, weights)

    st.subheader("🎯 Podsumowanie Portfela")
    col1, col2, col3 = st.columns(3)
    col1.metric(label=f"Portfel VaR Hist. ({confidence:.0%})", value=f"{port_var_hist:.2%}")
    col2.metric(label=f"Portfel VaR Param. ({confidence:.0%})", value=f"{port_var_param:.2%}")
    col3.caption(f"**Struktura wag:** {', '.join([f'{t}: {w:.0%}' for t, w in zip(tickers, weights)])}")

    st.divider()

    var_hist = value_at_risk_historical(returns, confidence_interval=confidence)
    var_param = value_at_risk_parametrical(returns, confidence_interval=confidence)
    es_hist = expected_shortfall(returns, historical_var=var_hist)
    sharpe = sharpe_ratio(returns)
    mdd = MDD(prices)

    st.subheader(f"📊 Metryki ryzyka dla poszczególnych spółek (Poziom ufności: {confidence:.0%})")
    summary_df = pd.DataFrame({"Waga": weights, "VaR Hist.": var_hist, "VaR Param.": var_param, "Expected Shortfall": es_hist, "Sharpe Ratio": sharpe, "Max Drawdown": mdd}, index=tickers)

    st.dataframe(summary_df.style.format({"Waga": "{:.1%}", "VaR Hist.": "{:.2%}", "VaR Param.": "{:.2%}", "Expected Shortfall": "{:.2%}", "Sharpe Ratio": "{:.2f}", "Max Drawdown": "{:.2%}"}), use_container_width=True)

    st.subheader("📈 Rozkład stóp zwrotu (KDE)")
    fig_kde = kde_plot(returns, var=var_hist, cvar=es_hist)
    st.pyplot(fig_kde)