from fastapi import APIRouter

router = APIRouter()

@router.post("/billing")
def generate_bill(customer_id: int, product_id: int):

    return {
        "status": "Payment Successful",
        "customer_id": customer_id,
        "product_id": product_id,
        "bill_status": "Paid",
        "exit_permission": "Allowed"
    }
