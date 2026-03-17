"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            Company: SpudWorks.
                        Program Name: SpudInference.
      Description: A low-end CPU friendly Local LLM Inference module.
                             File: main.py
                            Date: 2026/03/16
                        Version: 0.1.0-2026.03.16

===============================================================================

                        Copyright (C) 2026 SpudWorks Labs.

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU Affero General Public License as published
        by the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU Affero General Public License for more details.

        You should have received a copy of the GNU Affero General Public License
        along with this program. If not, see <https://www.gnu.org/licenses/>

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from llama_cpp import Llama


def speculative_step(main_model, draft_model, current_tokens, lookahead=5):
    draft_seq = []
    temp_context = list(current_tokens)

    for _ in range(lookahead):
        token = get_next_token(draft_model, temp_context)
        draft_seq.append(token)
        temp_context.append(token)

    main_model.eval(draft_seq)
    accepted_this_round = []
    
    for look in range(lookahead):
        slot_index = main_model.n_tokens - (lookahead - look)
        best_main_token = np.argmax(main_model._scores[slot_index - 1, :])

        if draft_seq[look] == best_main_token:
            accepted_this_round.append(best_main_token)

            if best_main_token == main_model.token_eos():
                return accepted_this_round, True
        
        else:
            accepted_this_round.append(best_main_token)
            return accepted_this_round, False

    extra_token = np.argmax(main_model._scores[main_model.n_tokens - 1, :])
    accepted_this_round.append(extra_token)

    return accepted_this_round, extra_token == main_model.token_eos()


def get_next_token(model, tokens):
    model.eval(tokens)
    logits = models._scores[model.n_tokens - 1, :]
    return np.argmax(logits)


def speculative_generate(main_model, draft_model, prompt, lookahead=5):
    tokens = main_model.tokenize(prompt.encode('utf-8'))

    main_model.eval(tokens)
    draft_model.eval(tokens)

    generated_text = ""

    while True:
        accepted_tokens, terminal_found = speculative_step(
            main_model, draf_model, tokens, lookahead
        )

        new_text = main_model.detokenize(accepted_tokens).decode('utf-8', errors='ignore')
        print(new_text, end='', flush=True)

        tokens.extend(accepted_tokens)
        draft_model.n_tokens = len(tokens)

        if terminal_found or len(tokens) > 500:
            print("\n\n\tInference has finished!")
            break


def main():
    main_model = Llama(model_path="models/Qwen3.5-9B-Q4_K_M.gguf", logits_all=True, n_ctx=2048)
    draft_model = Llama(model_path="models/Qwen3.5-0.8B-Q8_0.gguf", n_ctx=2048)

    speculative_generate(main_model, draft_model, "Hello, how are you?")

