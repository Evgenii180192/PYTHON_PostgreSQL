import psycopg2
from loguru import logger
from config import host, port, password, db_name, user

connection = None
cursor = None

try:
    logger.info("Database connection.")
    connection = psycopg2.connect(
        host=host,
        port=port,
        password=password,
        database=db_name,
        user=user
    )

    with connection.cursor() as cursor:
        def query_execution(sql_query):
            cursor.execute(sql_query)
            for items in cursor.fetchall():
                print(items)
            connection.commit()
            return logger.info("SQL query completed successfully.")


        # 1. Вывести всех работников чьи зарплаты есть в базе, вместе с зарплатами:
        query_execution("select employees.employee_name, salary.monthly_salary from employee_salary \
                        inner join salary on employee_salary.salary_id = salary.id \
                        inner join employees on employee_salary.employee_id = employees.id;")

        # 2. Вывести всех работников у которых ЗП меньше 2000:
        query_execution("select employee_name, monthly_salary from employees \
                        inner join employee_salary on employee_salary.employee_id = employees.id \
                        inner join salary on employee_salary.salary_id = salary.id \
                        where monthly_salary < 2000;")

        # 3. Вывести все зарплатные позиции, но работник по ним не назначен. (ЗП есть, но не понятно кто её получает.):
        query_execution("select salary.monthly_salary, employees.employee_name from employee_salary \
                        left join salary on employee_salary.salary_id = salary.id \
                        left join employees on employee_salary.employee_id = employees.id;")

        # 4. Вывести все зарплатные позиции  меньше 2000 но работник по ним не назначен. (ЗП есть, но не понятно кто
        # её получает.):
        query_execution("select salary.monthly_salary, employees.employee_name from employee_salary \
                        left join salary on employee_salary.salary_id = salary.id \
                        left join employees on employee_salary.employee_id = employees.id \
                        where salary.monthly_salary < 2000;")

        # 5. Найти всех работников кому не начислена ЗП:
        query_execution("select employees.employee_name, salary.monthly_salary from employee_salary \
                        right join salary on employee_salary.salary_id = salary.id \
                        right join employees on employee_salary.employee_id = employees.id;")

        # 6. Вывести всех работников с названиями их должности:
        query_execution("select employee_name, role_name from roles_employee \
                        inner join employees on roles_employee.employee_id = employees.id \
                        inner join roles  on roles_employee.role_id = roles.id;")

        # 7. Вывести имена и должность только Java разработчиков:
        query_execution("select employee_name, role_name from roles_employee \
                        inner join employees on roles_employee.employee_id = employees.id \
                        inner join roles on roles_employee.role_id = roles.id \
                        where role_name like '%Java %';")

        # 8. Вывести имена и должность только Python разработчиков:
        query_execution("select employee_name, role_name from roles_employee \
                        inner join roles on roles_employee.role_id = roles.id \
                        inner join employees on roles_employee.employee_id = employees.id \
                        where role_name like '%Python%';")

        # 9. Вывести имена и должность всех QA инженеров:
        query_execution("select employee_name, role_name from roles_employee \
                        inner join roles on roles_employee.role_id = roles.id \
                        inner join employees on roles_employee.employee_id = employees.id \
                        where role_name like '%QA%';")

        # 10. Вывести имена и должность ручных QA инженеров (Manual QA):
        query_execution("select employee_name, role_name from roles_employee \
                        inner join roles on roles_employee.role_id = roles.id \
                        inner join employees on roles_employee.employee_id = employees.id \
                        where role_name like '%Manual%QA%';")

        # 11. Вывести имена и должность автоматизаторов QA (Automation QA):
        query_execution("select employee_name, role_name from roles_employee \
                        inner join roles on roles_employee.role_id = roles.id \
                        inner join employees on roles_employee.employee_id = employees.id \
                        where role_name like '%Automation QA%';")

        # 12. Вывести имена и зарплаты Junior специалистов:
        query_execution("select employee_name, monthly_salary from employees \
                        inner join employee_salary on employee_salary.employee_id = employees.id \
                        inner join salary on employee_salary.salary_id = salary.id \
                        inner join roles_employee on roles_employee.employee_id = employees.id \
                        inner join roles on roles_employee.role_id = roles.id \
                        where role_name like '%Junior%';")

        # 13. Вывести имена и зарплаты Middle специалистов:
        query_execution("select employee_name, monthly_salary, role_name from employee_salary \
                        inner join salary on employee_salary.salary_id = salary.id \
                        inner join employees on employee_salary.employee_id = employees.id \
                        inner join roles_employee on roles_employee.employee_id = employees.id \
                        inner join roles on roles_employee.role_id = roles.id \
                        where role_name like '%Middle%';")

        # 14. Вывести имена и зарплаты Senior специалистов:
        query_execution("select employee_name, monthly_salary, role_name from employees \
                        inner join employee_salary on employee_salary.employee_id = employees.id \
                        inner join salary on employee_salary.salary_id = salary.id \
                        inner join roles_employee on roles_employee.employee_id = employees.id \
                        inner join roles on roles_employee.role_id = roles.id \
                        where role_name like '%Senior%';")

        # 15. Вывести зарплаты Java разработчиков:
        query_execution("select monthly_salary, role_name from employees \
                        inner join employee_salary on employee_salary.employee_id = employees.id \
                        inner join salary on employee_salary.salary_id = salary.id \
                        inner join roles_employee on roles_employee.employee_id = employees.id \
                        inner join roles on roles_employee.role_id = roles.id \
                        where role_name like '%Java%';")

        # 16. Вывести зарплаты Python разработчиков:
        query_execution("select monthly_salary, role_name from employees \
                        inner join employee_salary on employee_salary.employee_id = employees.id \
                        inner join salary on employee_salary.salary_id = salary.id \
                        inner join roles_employee on roles_employee.employee_id = employees.id \
                        inner join roles on roles_employee.role_id = roles.id \
                        where role_name like '%Python%';")

        # 17. Вывести имена и зарплаты Junior Python разработчиков:
        query_execution("select employee_name, monthly_salary from employees \
                        inner join employee_salary on employee_salary.employee_id = employees.id \
                        inner join salary on employee_salary.salary_id = salary.id \
                        inner join roles_employee on roles_employee.employee_id = employees.id \
                        inner join roles on roles_employee.role_id = roles.id \
                        where role_name like '%Junior Python%'; ")

        # 18. Вывести имена и зарплаты Middle JS разработчиков:
        query_execution("select employee_name, monthly_salary from employees \
                        inner join employee_salary on employee_salary.employee_id = employees.id \
                        inner join salary on employee_salary.salary_id = salary.id \
                        inner join roles_employee on roles_employee.employee_id = employees.id \
                        inner join roles on roles_employee.role_id = roles.id \
                        where role_name like '%Middle%J%S%'")

        # 19. Вывести имена и зарплаты Senior Java разработчиков:
        query_execution("select employee_name, monthly_salary from employees \
                        inner join employee_salary on employee_salary.employee_id = employees.id \
                        inner join salary on employee_salary.salary_id = salary.id \
                        inner join roles_employee on roles_employee.employee_id = employees.id \
                        inner join roles on roles_employee.role_id = roles.id \
                        where role_name like '%enior%J%S%'; ")

        # 20. Вывести зарплаты Junior QA инженеров:
        query_execution("select employee_name, monthly_salary, role_name from employees \
                        inner join employee_salary on employee_salary.employee_id = employees.id \
                        inner join salary on employee_salary.salary_id = salary.id \
                        inner join roles_employee on roles_employee.employee_id = employees.id \
                        inner join roles on roles_employee.role_id = roles.id \
                        where role_name like '%unior%QA%'")

        # 21. Вывести среднюю зарплату всех Junior специалистов:
        query_execution("select avg(salary.monthly_salary) from roles_employee \
                        join roles on roles_employee.role_id = roles.id \
                        join employee_salary on employee_salary.employee_id = roles_employee.employee_id \
                        join salary on employee_salary.salary_id = salary.id \
                        where role_name like '%unior%'")

        # 22. Вывести сумму зарплат JS разработчиков:
        query_execution("select sum(monthly_salary) from roles_employee \
                        inner join roles on roles_employee.role_id = roles.id \
                        inner join employee_salary on roles_employee.employee_id = employee_salary.employee_id \
                        inner join salary on employee_salary.salary_id = salary.id \
                        where role_name like '%J%S%dev%'")

        # 23. Вывести минимальную ЗП QA инженеров:
        query_execution("select min(monthly_salary) from roles_employee \
                        inner join roles on roles_employee.role_id = roles.id \
                        inner join employee_salary on roles_employee.employee_id = employee_salary.employee_id \
                        inner join salary on employee_salary.salary_id = salary.id \
                        where role_name like '%QA%';")

        # 24. Вывести максимальную ЗП QA инженеров:
        query_execution("select max(salary.monthly_salary) from roles_employee \
                        join roles on roles_employee.role_id = roles.id \
                        join employee_salary on employee_salary.employee_id = roles_employee.employee_id \
                        join salary on employee_salary.salary_id = salary.id \
                        where role_name like '%QA%';")

        # 25. Вывести количество QA инженеров:
        query_execution("select count (role_name) from roles \
                        inner join roles_employee on roles_employee.role_id = roles.id \
                        inner join employees on employees.id = roles_employee.employee_id \
                        where role_name like '%QA%';")

        # 26. Вывести количество Middle специалистов:
        query_execution("select count (role_name) from roles \
                        inner join roles_employee on roles_employee.role_id = roles.id \
                        inner join employees on employees.id = roles_employee.employee_id \
                        where role_name like '%Middle%';")

        # 27. Вывести количество разработчиков:
        query_execution("select count(role_name) from roles \
                        join roles_employee on roles_employee.role_id = roles.id \
                        join employees on roles_employee.employee_id = employees.id \
                        where role_name like '%develop%';")


        # 28. Вывести фонд (сумму) зарплаты разработчиков:
        query_execution("select sum(monthly_salary) from salary \
                        join employee_salary on employee_salary.salary_id = salary.id \
                        join roles_employee on employee_salary.employee_id = roles_employee.role_id \
                        inner join roles on roles_employee.role_id = roles.id \
                        where role_name like '%devel%';")

        # 29. Вывести имена, должности и ЗП всех специалистов по возрастанию:
        query_execution("select employee_name emloyee_name, role_name, monthly_salary from employees \
                        inner join employee_salary on employee_salary.employee_id = employees.id \
                        inner join salary on employee_salary.salary_id = salary.id \
                        inner join roles_employee on roles_employee.employee_id = employees.id \
                        inner join roles on roles_employee.role_id = roles.id \
                        order by monthly_salary ASC;")

        # 30. Вывести имена, должности и ЗП всех специалистов по возрастанию у специалистов у которых ЗП от 1700 до 2300:
        query_execution("select employee_name emloyee_name, role_name, monthly_salary from employees \
                        inner join employee_salary on employee_salary.employee_id = employees.id \
                        inner join salary on employee_salary.salary_id = salary.id \
                        inner join roles_employee on roles_employee.employee_id = employees.id \
                        inner join roles on roles_employee.role_id = roles.id \
                        where monthly_salary between 1700 and 2300 \
                        order by monthly_salary asc;")

        # 31. Вывести имена, должности и ЗП всех специалистов по возрастанию у специалистов у которых ЗП меньше 2300:
        query_execution("select employee_name emloyee_name, role_name, monthly_salary from employees \
                        inner join employee_salary on employee_salary.employee_id = employees.id \
                        inner join salary on employee_salary.salary_id = salary.id \
                        inner join roles_employee on roles_employee.employee_id = employees.id \
                        inner join roles on roles_employee.role_id = roles.id \
                        where monthly_salary < 2300 \
                        order by monthly_salary asc;")


        # 32. Вывести имена, должности и ЗП всех специалистов по возрастанию у специалистов у которых ЗП равна 1100, 1500, 2000:
        query_execution("select employee_name emloyee_name, role_name, monthly_salary from employees \
                        inner join employee_salary on employee_salary.employee_id = employees.id \
                        inner join salary on employee_salary.salary_id = salary.id \
                        inner join roles_employee on roles_employee.employee_id = employees.id \
                        inner join roles on roles_employee.role_id = roles.id \
                        where monthly_salary in (1100, 1500, 2000) \
                        order by monthly_salary asc;")


except Exception:
    logger.error("Failed to connect to database.")

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
