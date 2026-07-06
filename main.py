from savart_lite.inputs import collect_profile
from savart_lite.modules.health_score import calculate_health_score
from savart_lite.reports.text_report import write_report
from savart_lite.reports.charts import save_pie_chart, save_bar_chart


def main():
    profile = collect_profile()

    result = calculate_health_score(profile)

    write_report(profile, result)

    save_pie_chart(profile)
    save_bar_chart(result)

    print("\nFinancial Health Check Completed Successfully!")


if __name__ == "__main__":
    main()