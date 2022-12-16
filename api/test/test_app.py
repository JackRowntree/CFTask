def test_request_example(client):
    response = client.get("/read/first-chunk")
    print(response.data)
    assert b'{"data": {"data": "data"}}' == response.data