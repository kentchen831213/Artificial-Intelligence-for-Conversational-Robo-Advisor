# import aiml
from getData.aiml import Kernel  # Use PyAiml dev
import sys

# Create a Kernel object.
def runAIML(inpt):
    kernel = Kernel()
    kernel.bootstrap(brainFile = "getData/aiml-doc/aiwisfin_brain.brn")
    return kernel.respond(inpt)
