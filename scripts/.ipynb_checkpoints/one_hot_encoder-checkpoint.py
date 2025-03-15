import pandas as pd
from scripts.data_loader import load_data


def one_hot_encoder(file_path):
    df = pd.read_excel(file_path, sheet_name="Questionnaire")

    columns_to_encode = [
        'In the past six months, how many times have you attended a session or program on CSE topics?',
        'Do you think CSE should be taught to all adolescents and young people in schools?',
        'Before your first period, were you given any information about menstruation?',
        'Do you know how to calculate your menstrual cycle?',
        'What menstrual hygiene product(s) do you primarily use?',
        'How frequently do you change your menstrual hygiene product during a typical day of menstruation?',
        'Do you have access to safe and private facilities to manage menstruation (e.g., toilets, washing areas)?',
        'How often should a person be tested to know if they have HIV?',
        'What is PrEP (Pre-Exposure Prophylaxis)?',
        'How often does your school or community distribute educational materials about HIV or STI prevention?',
        'How often do they organise HIV campaigns in the town/village where you are living?',
        'Have you ever been tested for HIV?',
        'Are there youth-friendly clinics or services in your area that provide STI counseling and treatment?',
        'Do you know methods to prevent pregnancy?',
        'At what stage in the menstrual cycle is a woman most likely to get pregnant?',
        'Have you ever used any method to prevent unintended pregnancy?',
        'Do you know where they offer TB services in Tonga?',
        'Have you ever been screened for TB in the past 12 months?',
        'If you experience persistent coughing for more than two weeks, are you likely to visit a health facility?',
        'Do you feel comfortable seeking TB services from local health facilities?',
        'Have you received information about TB at a facility where you sought sexual and reproductive health services?',
        'Have you faced any challenges accessing TB services  in the past year?',
        'Do you think malaria can be linked to HIV or affect people living with HIV differently?',
        'How often do you sleep under an insecticide-treated mosquito net?',
        'The last time you had a fever; did you get tested for malaria at a health facility?',
        'Do you know where to access mosquito nets?',
        'Have you taken anti-malaria drugs in the past 12 months?',
    ]

    responses_to_map = {
        '1–2 times': 0, '3–5 times': 1, 'More than 5 times': 2, 'Never': 3,
        'Strongly agree': 0, 'Agree': 1, 'Neutral': 2, 'Disagree': 3, 'Strongly disagree': 4,
        'Disposable sanitary pads': 0, 'Reusable cloth pads': 1, 'Menstrual cups': 2, 'Natural materials (e.g., leaves, cloth)': 3,
        '3–4 times': 1, '5 or more times': 2, 'Do not change regularly': 3,
        'Yes': 1, 'No': 0, 'Yes, always': 0, 'Yes, sometimes': 2,
        'Every 3–6 months': 0, 'Once a year': 1, 'Only when symptoms appear': 2, "I don't know": 4,
        'A vaccine to prevent HIV': 1, 'A daily pill to reduce HIV risk': 2,
        'Very often(e.g., monthly or more frequently)': 0, 'Occasionally(e.g., a few times a year)': 1, 'Rarely(e.g., once a year or less)': 2, 'Others (please specify)': 5,
        'During her period': 1, 'Right before her period': 2, 'In the middle of her period': 3,
        'Yes, I currently use contraception': 0, 'Yes, but I am not currently using contraception': 1, 'No, but I am interested in using contraception': 2, 'No, I do not use contraception': 3,
        'Yes, I feel comfortable.': 0, 'No, I do not feel comfortable.': 1,
        "I'm not sure": 2,
        'Every night': 0, 'Occasionally': 1, 'Rarely': 2,
        'Yes, immediately': 0, 'Yes, but after several days': 1, 'No, I self-medicated': 2, 'No, I did not seek any treatment': 3,
        'Yes, for prevention': 0, 'Yes, for treatment': 1, 'No, I have not taken any anti-malaria drugs': 2,
    }

    df[columns_to_encode] = df[columns_to_encode].apply(lambda x: x.map(responses_to_map))


    print("one hot encoding performed successfully")

    df.to_excel("data/project 2.xlsx", index=False, sheet_name="Questionnaire")

    df = load_data("data/project 2.xlsx")

    return df