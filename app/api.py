from config import APP_TOKEN, APP_SECRET
import requests

class cdcApi:
    def __init__(self):
        self.columns = []
        self.headers = {
            "Host": "data.cdc.gov",
            "Accept": "application/json",
            "X-App-Token": APP_TOKEN
        }
        self.url = ""

    def query(self,params):
        response = requests.get(
            self.url,
            headers=self.headers,
            params=params
        )
        response.raise_for_status()
        response_json = response.json()
        return response_json


### Public surveillence data
### https://dev.socrata.com/foundry/data.cdc.gov/vbim-akqf
class cdcSurv(cdcApi):
    def __init__(self):
        super().__init__()
        self.columns = [
            "cdc_report_dt",
            "pos_spec_dt",
            "onset_dt",
            "current_status",
            "sex",
            "age_group",
            "race_ethnicity_combined",
            "hosp_yn",
            "icu_yn",
            "death_yn",
            "medcond_yn"
        ]
        self.url = "https://data.cdc.gov/resource/vbim-akqf.json"

params = {
    "$limit":"100"
}

cs = cdcSurv()
surv_json = cs.query(params)


### US Cases & Deaths by State Over Time
### https://dev.socrata.com/foundry/data.cdc.gov/9mfq-cb36

class cdcState(cdcApi):
    def __init__(self):
        super().__init__()
        self.columns = [
            "submission_date",
            "state",
            "tot_cases",
            "conf_cases",
            "prob_cases",
            "new_case",
            "pnew_case",
            "tot_death",
            "conf_death",
            "prob_death",
            "new_death",
            "pnew_death",
            "created_at",
            "consent_cases",
            "consent_deaths"
        ]
        self.url = "https://data.cdc.gov/resource/9mfq-cb36.json"

params = {
    "$limit":"100"
}

cst = cdcState()
st_json = cst.query(params)

### Conditions contributing to deaths involving COVID-19
### https://dev.socrata.com/foundry/data.cdc.gov/hk9y-quqm

class cdcCond(cdcApi):
    def __init__(self):
        super().__init__()
### https://dev.socrata.com/foundry/data.cdc.gov/9mfq-cb36

class cdcState(cdcApi):
    def __init__(self):
        super().__init__()
        self.columns = [
            "data_as_of",
            "start_week",
            "end_week",
            "state",
            "condition_group",
            "condition",
            "icd10_codes",
            "age_group",
            "number_covid19_deaths",
            "flag"
        ]
        self.url = "https://data.cdc.gov/resource/9mfq-cb36.json"

params = {
    "$limit":"100"
}

ccd = cdcCond()
cond_json = cst.query(params)

