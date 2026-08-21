def run(payload=None):
 return {"system":"F82","status":"reference_analysis_ready","input":payload or {},"human_review_required":True}

if __name__ == "__main__": print(run())
