import json
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Command(BaseModel):
    command: str = Field(
        title="Command line",
        description="The command line to be passed to stress-ng",
        examples=[
            "--cpu 4 --vm 2 --hdd 1 --fork 8 --timeout 30s --metrics",
            "example 2",
            "example 3"
        ]
    )
    repetitions: int | None = Field(
        default=1,
        title="Number of repetitions",
        description="Number of iterations of the supplied stress-ng command",
        le=1000
    )


    # See https://fastapi.tiangolo.com/tutorial/schema-extra-example/ for how to support multiple examples

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "command": "--cpu 4 --vm 2 --hdd 1 --fork 8 --timeout 30s --metrics",
                    "repetitions": 5
                }
            ]
        }
    }

class Commands(BaseModel):
    commands: List[Command] = Field(
        title="Command list",
        description="List of commands to be executed using stress-ng"
    )

@app.get("/")
async def root():

    return {"message": "OK", "status": 200,  "error-message": None }


@app.post("/run")
async def run(commands: Commands):
    
    return commands



    