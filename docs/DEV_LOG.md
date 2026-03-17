# SpudInference; Developer Logs

## Logs
*2026/03/16*
* 16:43
    - Creating the boilerpate structure and laying out the foundations.

*2026/03/17*
* 04:05
    - Now creating the first test after compiling and quantizing the required models.

* 06:53
    - The test has been putinto `main.py`, I will test this tomorrow morning.

* 17:04
    - Added the missing `numpy` import.
    - Now ensuring the model files exist within the project.

* 17:11
    - The models are now in the right directory. (`models/`)
    - They have been symlinked there to save some space.

* 17:16
    - Updated the Project Structure Tree in the ARCHITECTURE.md
      document to reflect the structure updates.

* 21:36
    - Created the llama-cpp-python local module.
    - Also created the requests version that reaches the llama-server API.
      No I need to make the Thinking Model a bit faster.


## TO-DO
[!] Add an inference time function wrapper.
[!] A future download models from cloud/link option.
