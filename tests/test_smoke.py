from run import run

def test_smoke():
 assert run({})["system"] == "F82"
 assert run({})["human_review_required"] is True
