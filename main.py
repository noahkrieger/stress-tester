import asyncio
import itertools
import json
import subprocess
import time
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

import cpu_stressors

#from decorators import timeout

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


@app.post("/runng")
async def run(commands: Commands):
    retvals = []
    for command in commands.commands:
        for _ in range(command.repetitions):
            print('COMMAND: ', command.command)
            print('RUNNING: ', ["stress-ng"] + command.command.split())
            retvals.append(subprocess.run(["stress-ng"] + command.command.split(), stdout=subprocess.PIPE))
    
    return retvals



@app.get("/test")
async def test():

    async def loop():
        await asyncio.sleep(1)

    async def loop2():
        try:
            x = 0
            for _ in itertools.count():
                x += 1
                await asyncio.sleep(0)
        except asyncio.CancelledError as ex:
            print (f"{x} iterations")
            raise ex

    task = asyncio.create_task(cpu_stressors.euler2())        

    start = time.time()
    try:
        await asyncio.wait_for(task, timeout=0.5)
        raise HTTPException(400, "No timeout")
    except TimeoutError:
        return {"status": 200, "message": "Timeout at {:.3f}".format(time.time() - start)}
   


    


        
    


    