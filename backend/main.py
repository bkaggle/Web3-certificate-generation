# main.py

from fastapi import FastAPI, HTTPException, Depends, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from algosdk import account, mnemonic, transaction

app = FastAPI()

origins = ["http://localhost", "http://localhost:3000"]  # Add your frontend's origin(s)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Placeholder data for demonstration purposes
nft_data = {
    "nft_id": "123",
    "trainee_address": "ADDRESS_HERE",
    "nft_status": "issued",
}


class NFT(BaseModel):
    trainee_address: str


@app.post("/issue-nft")
def issue_nft(trainee: NFT):
    # Placeholder logic to issue NFT
    # In a real-world scenario, you would interact with the Algorand blockchain using the SDK
    nft_data["trainee_address"] = trainee.trainee_address
    nft_data["nft_status"] = "issued"
    return nft_data


@app.post("/opt-in")
def opt_in_to_nft(trainee: NFT):
    # Placeholder logic to handle trainee opting in to NFT
    # In a real-world scenario, you would interact with the Algorand blockchain using the SDK
    nft_data["nft_status"] = "opted-in"
    return nft_data


@app.post("/approve-transfer")
def approve_transfer(trainee: NFT):
    # Placeholder logic to handle approving transfer of NFT
    # In a real-world scenario, you would interact with the Algorand blockchain using the SDK
    nft_data["nft_status"] = "transfer-approved"
    return nft_data
