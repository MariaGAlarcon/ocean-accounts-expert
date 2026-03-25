# Training Materials: Compiling Coral Reef Condition Accounts

Training session for Belize Statistical Institute and Fisheries Department staff on how to produce SEEA EA condition accounts from AGRRA survey data.

## Session Plan (1.5 hours)

| Time | Activity | Materials |
|---|---|---|
| 0:00 to 0:20 | Presentation: what is a condition account, the 3 steps | `facilitator_guide.docx` |
| 0:20 to 0:30 | Guided example: normalize one site together | Facilitator guide, slides 6 to 8 |
| 0:30 to 1:10 | Hands-on exercise: Hol Chan Marine Reserve | `exercise_handout.docx` + `exercise_workbook.xlsx` |
| 1:10 to 1:30 | Review answers and discussion | `answer_key.xlsx` |

## Materials

| File | Description |
|---|---|
| `facilitator_guide.md` / `.docx` | Presentation content with speaker notes, slide by slide |
| `exercise_handout.md` / `.docx` | Printed handout for participants with instructions and blank tables |
| `exercise_workbook.xlsx` | Excel file with site data pre-loaded, calculation cells empty |
| `answer_key.xlsx` | Completed Excel file for comparison after the exercise |

## Prerequisites for Participants

Participants need a laptop with Excel 2016 or later. No R or programming knowledge is required. The exercise uses data from 4 survey sites in Hol Chan Marine Reserve across 2 years (2023 and 2025).

## Regenerating the Excel Files

Run `python3 generate_exercise_workbooks.py` from this directory to regenerate the exercise workbook and answer key.
