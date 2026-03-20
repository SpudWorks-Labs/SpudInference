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

*2026/03/20*
* 05:34
    - Starting to create the tool menu.

* 05:46
    - Changing the Project structure to allow for the tools.

* 06:01
    - Updated the `ARCHITECTURE.md` to reflect the Project Tree updates.
    - Changed the main program into a `textual` TUI. (Might go back to regular TUI for simplicity)

- 18:51
    - Updated the `README.md` to reflect what the actual current program is.
    - Need to add a project map. (Maybe in the ARCHITECTURE, but I also need to link that)
    - The `ARCHITECTURE.md` now needs to be updated to reflect the actual architecture.

* 21:10
    - Finished updating the `ARCHITECTURE.md` and now pushing to the repo.


## TO-DO
[!] Need to have a folder for generated files. (train.txt, datasets, etc.)
[.] Add an inference time function wrapper.
[.] A future download models from cloud/link option.
