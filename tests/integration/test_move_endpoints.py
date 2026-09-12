def test_move_round_trip(client):
    moves = "15F6B6B5L16R8B16F20L6F13F11R"
    
    res = client.post(
        "/adventurers/adventurer-1/make_moves",
        json={"moves": moves},
    )
    assert res.status_code == 201
    assert len(res.get_json()) == 11
    
    moves_response = client.get("/adventurers/adventurer-1/get_moves")
    assert moves_response.status_code == 200
    assert len(moves_response.get_json()) == 11


def test_get_moves_for_unknown_adventurer_returns_404(client):
    response = client.get("/adventurers/does-not-exist/get_moves")
    assert response.status_code == 404
