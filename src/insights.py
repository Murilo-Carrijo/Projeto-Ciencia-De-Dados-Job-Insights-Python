from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    list_of_unique_type = []
    for line in data:
        types = line.get("job_type")
        list_of_unique_type.append(types)
    job_type = set(list_of_unique_type)
    return job_type


def filter_by_job_type(jobs, job_type):
    list_filter = []
    for job in jobs:
        if job["job_type"] == job_type:
            list_filter.append(job)
    return list_filter


def get_unique_industries(path):
    data = read(path)
    list_of_unique_industry = []
    for line in data:
        industries = line.get("industry")
        if industries != "":
            list_of_unique_industry.append(industries)
    industry = set(list_of_unique_industry)
    return industry


def filter_by_industry(jobs, industry):
    list_filter = []
    for job in jobs:
        if job["industry"] == industry:
            list_filter.append(job)
    return list_filter


def get_max_salary(path):
    data = read(path)
    max_salary = 0
    for line in data:
        check_salary = line["max_salary"].isdigit()
        if check_salary:
            salary = int(line["max_salary"])
        else:
            salary = 0
        if salary >= max_salary:
            max_salary = salary
    return max_salary


# teste de execução da função get_max_salary


# if __name__ == "__main__":
#     salary = get_max_salary("src/jobs.csv")
#     print(salary)


def get_min_salary(path):
    data = read(path)
    all_salary = []
    for line in data:
        check_salary = line["min_salary"].isdigit()
        if check_salary:
            all_salary.append(int(line["min_salary"]))
    min_salary = all_salary[0]
    for salary in all_salary:
        if salary <= min_salary:
            min_salary = salary
    return min_salary


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Salário mínimo ou máximo pendente")
    elif (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError("Os valores não são nº inteiros")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("Salário mínimo maior que o salário máximo")
    elif job["min_salary"] <= salary and job["max_salary"] >= salary:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    result_filter = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                result_filter.append(job)
        except ValueError:
            pass

    return result_filter
