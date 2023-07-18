import streamlit as st
import joblib

model = joblib.load('model1.pkl')

@st.cache
def predict_backorder(national_inv, lead_time, sales_1_month, pieces_past_due, perf_6_month_avg,
                      in_transit_qty, local_bo_qty, deck_risk, oe_constraint, ppap_risk,
                      stop_auto_buy, rev_stop):
    values = [national_inv, lead_time, sales_1_month, pieces_past_due, perf_6_month_avg,
              in_transit_qty, local_bo_qty, deck_risk, oe_constraint, ppap_risk,
              stop_auto_buy, rev_stop]
    arr = [values]
    acc = model.predict(arr)

    if acc[0] == 0:
        return "Product went on Backorder"
    else:
        return "Did not go on backorder"

def main():
    st.title("Backorder Prediction")

    national_inv = st.number_input("National Inventory", min_value=0)
    lead_time = st.number_input("Lead Time", min_value=0)
    sales_1_month = st.number_input("Sales in 1 Month", min_value=0)
    pieces_past_due = st.number_input("Pieces Past Due", min_value=0)
    perf_6_month_avg = st.number_input("Performance 6 Month Avg", min_value=0)
    in_transit_qty = st.number_input("In Transit Quantity", min_value=0)
    local_bo_qty = st.number_input("Local BO Quantity", min_value=0)
    deck_risk = st.number_input("Deck Risk", min_value=0, max_value=1, step=1)
    oe_constraint = st.number_input("OE Constraint", min_value=0, max_value=1, step=1)
    ppap_risk = st.number_input("PPAP Risk", min_value=0, max_value=1, step=1)
    stop_auto_buy = st.number_input("Stop Auto Buy", min_value=0, max_value=1, step=1)
    rev_stop = st.number_input("Revenue Stop", min_value=0, max_value=1, step=1)

    if st.button("Predict"):
        result = predict_backorder(national_inv, lead_time, sales_1_month, pieces_past_due,
                                   perf_6_month_avg, in_transit_qty, local_bo_qty,
                                   deck_risk, oe_constraint, ppap_risk,
                                   stop_auto_buy, rev_stop)
        st.write("Prediction:", result)

if __name__ == '__main__':
    main()
