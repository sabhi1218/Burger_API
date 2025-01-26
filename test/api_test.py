from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_stock():
    pre_response = client.get("/stock/")
    # try:
    bun = pre_response.json()["bun"]
    # except:
    #     bun = 0
    response = client.post("/stock/", json={"item": "bun", "quantity": 10})
    assert response.status_code == 201
    assert response.json()["item"] == "bun"
    assert response.json()["quantity"] == 10+bun

def test_get_burger_count():
    pre_response = client.get("/burgers/")
    burgers = pre_response.json()["burgers"]
    client.post("/stock/", json={"item": "bun", "quantity": 5})
    client.post("/stock/", json={"item": "patty", "quantity": 5})
    client.post("/stock/", json={"item": "lettuce", "quantity": 5})
    client.post("/stock/", json={"item": "tomato", "quantity": 5})
    client.post("/stock/", json={"item": "ketchup", "quantity": 5})
    response = client.get("/burgers/")
    assert response.status_code == 200
    assert response.json()["burgers"] == 5+burgers
