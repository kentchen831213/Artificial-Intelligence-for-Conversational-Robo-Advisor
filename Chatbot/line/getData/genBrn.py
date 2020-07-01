import aiml
import os

kernel = aiml.Kernel()
kernel.bootstrap(learnFiles = "./aiml-doc/std-startup.xml", commands = "load aiml b")
kernel.saveBrain("./aiml-doc/aiwisfin_brain.brn")
