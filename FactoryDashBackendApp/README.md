<h4>Запросы</h4>  

GET /api/workshops
RETURN: JSON
{
    "workshops": [{"id": int, "name": str}]
}
- workshops: список цехов
- - id: int, id цеха
- - name: str, название цеха

GET /api/machines/workshop_id
- workshop_id: int, id цеха
RETURN: JSON
{
    "machines": [{"id": int, "name": str}]
}
- workshops: список станков в заданном цеху
- - id: int, id станка
- - name: str, название станка

GET /api/machine_schedule?start_date={}&end_date={}&[workshop_id|machine_id]={}
Обазательно должен быть передан один из:  
- workshop_id: int, id цеха
- machine_id: int, id станка
Опциональные, по умолчанию начало плана + 14 дней
- start_date: datetime, начало времени за которое нужны данные
- end_date: datetime, конецвремени за которое нужны данные
RETURN: JSON  
{
states: [
  {
    "machine": str,
    "occupied": [int]
  }
],
"days":["%d.%m.%Y"]
}
- states: список состояния станков
- - machine: str, наименование станка
- - occupied: List[str], список загруженности в процентах на каждый день
- "days": List[str], даты за которые выдана загрузка станков, формат день.месяц.год

GET /api/kpi_index_value/kpi_area_id
- kpi_area_id: int, id области KPI
{
  "kpi_indexes": [
    {
      "gradingData": [
        {
          "color": str,
          "highScore": int,
          "lowScore": int
        },
      ],
      "name": str,
      "score": float
    }
  ]
}
- kpi_indexes: список показаний KPI индеков
- - name: str, наименование индека KPI
- - score: float, показатель KPI
- - gradingData: зоны "угрозы" для индекса
- - - color: str, цвет зоны, формат #ffffff
- - - highScore, lowScore: int, границы зоны