<script>
import axios from "../axios/index.js";
import 'animate.css';
import Info from "../components/map/ui/Info.vue";
import LinedChart from "../components/map/ui/charts/LinedChart.vue";
import PolarChart from "../components/map/ui/charts/PolarChart.vue";
import BarChart from "../components/map/ui/charts/BarChart.vue";
import RadarChart from "../components/map/ui/charts/RadarChart.vue";
import ChartsStatistic from "../components/map/ChartsStatistic.vue";
import MainTitle from "../components/ui/MainTitle.vue";
import DistricsFilter from "../components/map/ui/filters/DistricsFilter.vue";
import TypesFilter from "../components/map/ui/filters/TypesFilter.vue";
import DatePicker from "../components/map/ui/filters/DatePicker.vue";
import SvgMap from "../components/map/SvgMap.vue";
import Tooltip from "../components/ui/Tooltip.vue";
import AdminHeader from "../components/admin/AdminHeader.vue";

export default {
  name: "Map",
  components: {
    AdminHeader,
    Tooltip,
    SvgMap,
    DatePicker,
    TypesFilter,
    DistricsFilter, MainTitle, ChartsStatistic, RadarChart, BarChart, PolarChart, LinedChart, Info
  },
  data() {
    return {
      districts: [],
      activeDistrict: {},
      currentDistrict: '',
      activeFilter: {},
      activeAnalyze: {},
      dates: {
        from: '',
        to: ''
      },
      analyzes: [
        {
          name: 'Урожайность',
          datasets: [
            {
              label: 'Диаграмма рассеяния между содержанием органического вещества и уровнем pH.',
              backgroundColor: '#f87979',
              data: [40, 39, 10, 40, 39, 80, 40],
              fill: false,
              borderColor: '#f87979',
              tension: 0.1
            },
            {
              label: 'Карта распределения pH по полю.',
              backgroundColor: '#da7827',
              data: [39, 20, 5, 67, 4, 56, 0],
              fill: false,
              borderColor: '#da7827',
              tension: 0.1
            }
          ],
          polarAnalyzes: {
            title: 'Исследование',
            labels: [
              'Оксиды железа',
              'Глины',
              'Карбонаты',
              'Сульфиды',
              'Фосфориты',
              'Силикаты',
              'Соли'
            ],
            datasets: [
              {
                label: 'Типы минералов',
                data: [65, 59, 90, 81, 56, 55, 40],
                backgroundColor: [
                  'rgb(255, 99, 132)',
                  'rgb(75, 192, 192)',
                  'rgb(255, 205, 86)',
                  'rgb(201, 203, 207)',
                  'rgb(54, 162, 235)',
                  'rgb(153, 102, 255)',
                  'rgb(255, 159, 64)'
                ],
                borderColor: [
                  'rgba(255, 255, 255, 1)',
                ],
                borderWidth: 2
              }
            ]
          },
          barAnalyzes: {
            title: 'Исследование',
            labels: [
              'Арбуз',
              'Дыня',
              'Помидоры',
              'Картофель',
              'Морковь',
              'Лук',
              'Кукуруза',
              'Пшеница',
              'Рис',
              'Ячмень',
              'Овес',
              'Хлопок'
            ],
            datasets: [
              {
                label: 'Результаты урожая за период',
                data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 99],
                backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(255, 159, 64, 0.2)',
                  'rgba(255, 205, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(102, 255, 102, 0.2)',
                  'rgba(255, 128, 0, 0.2)',
                  'rgba(128, 0, 255, 0.2)',
                  'rgba(255, 128, 192, 0.2)',
                  'rgba(255, 51, 153, 0.2)'
                ],
                borderColor: [
                  'rgb(255, 99, 132)',
                  'rgb(255, 159, 64)',
                  'rgb(255, 205, 86)',
                  'rgb(75, 192, 192)',
                  'rgb(54, 162, 235)',
                  'rgb(153, 102, 255)',
                  'rgb(255, 206, 86)',
                  'rgb(102, 255, 102)',
                  'rgb(255, 128, 0)',
                  'rgb(128, 0, 255)',
                  'rgb(255, 128, 192)',
                  'rgb(255, 51, 153)'
                ],
                borderWidth: 1
              }
            ]
          },
          radarAnalyzes: {
            title: 'Исследование',
            labels: ['Температура почвы', 'Влажность', 'Питательные вещества', 'Кислотность', 'Плотность почвы', 'Солнечное излучение', 'Частота осадков', 'Активность ферментов'],
            datasets: [
              {
                label: 'Весна',
                data: [65, 80, 70, 90, 75, 75, 75, 98],
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgb(54, 162, 235)'
              },
              {
                label: 'Осень',
                data: [50, 75, 85, 60, 34, 56, 67, 95],
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgb(255, 99, 132)'
              }
            ]
          }
        },
        {
          name: 'Проблемные зоны',
          datasets: [
            {
              label: 'Диаграмма рассеяния между содержанием органического вещества и уровнем pH.',
              backgroundColor: '#f87979',
              data: [40, 39, 10, 40, 39, 80, 40],
              fill: false,
              borderColor: '#f87979',
              tension: 0.1
            },
            {
              label: 'Карта распределения pH по полю.',
              backgroundColor: '#da7827',
              data: [39, 20, 5, 67, 4, 56, 0],
              fill: false,
              borderColor: '#da7827',
              tension: 0.1
            }
          ],
          polarAnalyzes: {
            title: 'Исследование',
            labels: [
              'Оксиды железа',
              'Глины',
              'Карбонаты',
              'Сульфиды',
              'Фосфориты',
              'Силикаты',
              'Соли'
            ],
            datasets: [
              {
                label: 'Типы минералов',
                data: [65, 59, 90, 81, 56, 55, 40],
                backgroundColor: [
                  'rgb(255, 99, 132)',
                  'rgb(75, 192, 192)',
                  'rgb(255, 205, 86)',
                  'rgb(201, 203, 207)',
                  'rgb(54, 162, 235)',
                  'rgb(153, 102, 255)',
                  'rgb(255, 159, 64)'
                ],
                borderColor: [
                  'rgba(255, 255, 255, 1)',
                ],
                borderWidth: 2
              }
            ]
          },
          barAnalyzes: {
            title: 'Исследование',
            labels: [
              'Арбуз',
              'Дыня',
              'Помидоры',
              'Картофель',
              'Морковь',
              'Лук',
              'Кукуруза',
              'Пшеница',
              'Рис',
              'Ячмень',
              'Овес',
              'Хлопок'
            ],
            datasets: [
              {
                label: 'Результаты урожая за период',
                data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 99],
                backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(255, 159, 64, 0.2)',
                  'rgba(255, 205, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(102, 255, 102, 0.2)',
                  'rgba(255, 128, 0, 0.2)',
                  'rgba(128, 0, 255, 0.2)',
                  'rgba(255, 128, 192, 0.2)',
                  'rgba(255, 51, 153, 0.2)'
                ],
                borderColor: [
                  'rgb(255, 99, 132)',
                  'rgb(255, 159, 64)',
                  'rgb(255, 205, 86)',
                  'rgb(75, 192, 192)',
                  'rgb(54, 162, 235)',
                  'rgb(153, 102, 255)',
                  'rgb(255, 206, 86)',
                  'rgb(102, 255, 102)',
                  'rgb(255, 128, 0)',
                  'rgb(128, 0, 255)',
                  'rgb(255, 128, 192)',
                  'rgb(255, 51, 153)'
                ],
                borderWidth: 1
              }
            ]
          },
          radarAnalyzes: {
            title: 'Исследование',
            labels: ['Температура почвы', 'Влажность', 'Питательные вещества', 'Кислотность', 'Плотность почвы', 'Солнечное излучение', 'Частота осадков', 'Активность ферментов'],
            datasets: [
              {
                label: 'Весна',
                data: [65, 80, 70, 90, 75, 75, 75, 98],
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgb(54, 162, 235)'
              },
              {
                label: 'Осень',
                data: [50, 75, 85, 60, 34, 56, 67, 95],
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgb(255, 99, 132)'
              }
            ]
          }
        },
        {
          name: 'Влажность почвы',
          datasets: [
            {
              label: 'Диаграмма рассеяния между содержанием органического вещества и уровнем pH.',
              backgroundColor: '#f87979',
              data: [40, 39, 10, 40, 39, 80, 40],
              fill: false,
              borderColor: '#f87979',
              tension: 0.1
            },
            {
              label: 'Карта распределения pH по полю.',
              backgroundColor: '#da7827',
              data: [39, 20, 5, 67, 4, 56, 0],
              fill: false,
              borderColor: '#da7827',
              tension: 0.1
            }
          ],
          polarAnalyzes: {
            title: 'Исследование',
            labels: [
              'Оксиды железа',
              'Глины',
              'Карбонаты',
              'Сульфиды',
              'Фосфориты',
              'Силикаты',
              'Соли'
            ],
            datasets: [
              {
                label: 'Типы минералов',
                data: [65, 59, 90, 81, 56, 55, 40],
                backgroundColor: [
                  'rgb(255, 99, 132)',
                  'rgb(75, 192, 192)',
                  'rgb(255, 205, 86)',
                  'rgb(201, 203, 207)',
                  'rgb(54, 162, 235)',
                  'rgb(153, 102, 255)',
                  'rgb(255, 159, 64)'
                ],
                borderColor: [
                  'rgba(255, 255, 255, 1)',
                ],
                borderWidth: 2
              }
            ]
          },
          barAnalyzes: {
            title: 'Исследование',
            labels: [
              'Арбуз',
              'Дыня',
              'Помидоры',
              'Картофель',
              'Морковь',
              'Лук',
              'Кукуруза',
              'Пшеница',
              'Рис',
              'Ячмень',
              'Овес',
              'Хлопок'
            ],
            datasets: [
              {
                label: 'Результаты урожая за период',
                data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 99],
                backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(255, 159, 64, 0.2)',
                  'rgba(255, 205, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(102, 255, 102, 0.2)',
                  'rgba(255, 128, 0, 0.2)',
                  'rgba(128, 0, 255, 0.2)',
                  'rgba(255, 128, 192, 0.2)',
                  'rgba(255, 51, 153, 0.2)'
                ],
                borderColor: [
                  'rgb(255, 99, 132)',
                  'rgb(255, 159, 64)',
                  'rgb(255, 205, 86)',
                  'rgb(75, 192, 192)',
                  'rgb(54, 162, 235)',
                  'rgb(153, 102, 255)',
                  'rgb(255, 206, 86)',
                  'rgb(102, 255, 102)',
                  'rgb(255, 128, 0)',
                  'rgb(128, 0, 255)',
                  'rgb(255, 128, 192)',
                  'rgb(255, 51, 153)'
                ],
                borderWidth: 1
              }
            ]
          },
          radarAnalyzes: {
            title: 'Исследование',
            labels: ['Температура почвы', 'Влажность', 'Питательные вещества', 'Кислотность', 'Плотность почвы', 'Солнечное излучение', 'Частота осадков', 'Активность ферментов'],
            datasets: [
              {
                label: 'Весна',
                data: [65, 80, 70, 90, 75, 75, 75, 98],
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgb(54, 162, 235)'
              },
              {
                label: 'Осень',
                data: [50, 75, 85, 60, 34, 56, 67, 95],
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgb(255, 99, 132)'
              }
            ]
          }
        },
        {
          name: 'Состояния растительности',
          datasets: [
            {
              label: 'Диаграмма рассеяния между содержанием органического вещества и уровнем pH.',
              backgroundColor: '#f87979',
              data: [40, 39, 10, 40, 39, 80, 40],
              fill: false,
              borderColor: '#f87979',
              tension: 0.1
            },
            {
              label: 'Карта распределения pH по полю.',
              backgroundColor: '#da7827',
              data: [39, 20, 5, 67, 4, 56, 0],
              fill: false,
              borderColor: '#da7827',
              tension: 0.1
            }
          ],
          polarAnalyzes: {
            title: 'Исследование',
            labels: [
              'Оксиды железа',
              'Глины',
              'Карбонаты',
              'Сульфиды',
              'Фосфориты',
              'Силикаты',
              'Соли'
            ],
            datasets: [
              {
                label: 'Типы минералов',
                data: [65, 59, 90, 81, 56, 55, 40],
                backgroundColor: [
                  'rgb(255, 99, 132)',
                  'rgb(75, 192, 192)',
                  'rgb(255, 205, 86)',
                  'rgb(201, 203, 207)',
                  'rgb(54, 162, 235)',
                  'rgb(153, 102, 255)',
                  'rgb(255, 159, 64)'
                ],
                borderColor: [
                  'rgba(255, 255, 255, 1)',
                ],
                borderWidth: 2
              }
            ]
          },
          barAnalyzes: {
            title: 'Исследование',
            labels: [
              'Арбуз',
              'Дыня',
              'Помидоры',
              'Картофель',
              'Морковь',
              'Лук',
              'Кукуруза',
              'Пшеница',
              'Рис',
              'Ячмень',
              'Овес',
              'Хлопок'
            ],
            datasets: [
              {
                label: 'Результаты урожая за период',
                data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 99],
                backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(255, 159, 64, 0.2)',
                  'rgba(255, 205, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(102, 255, 102, 0.2)',
                  'rgba(255, 128, 0, 0.2)',
                  'rgba(128, 0, 255, 0.2)',
                  'rgba(255, 128, 192, 0.2)',
                  'rgba(255, 51, 153, 0.2)'
                ],
                borderColor: [
                  'rgb(255, 99, 132)',
                  'rgb(255, 159, 64)',
                  'rgb(255, 205, 86)',
                  'rgb(75, 192, 192)',
                  'rgb(54, 162, 235)',
                  'rgb(153, 102, 255)',
                  'rgb(255, 206, 86)',
                  'rgb(102, 255, 102)',
                  'rgb(255, 128, 0)',
                  'rgb(128, 0, 255)',
                  'rgb(255, 128, 192)',
                  'rgb(255, 51, 153)'
                ],
                borderWidth: 1
              }
            ]
          },
          radarAnalyzes: {
            title: 'Исследование',
            labels: ['Температура почвы', 'Влажность', 'Питательные вещества', 'Кислотность', 'Плотность почвы', 'Солнечное излучение', 'Частота осадков', 'Активность ферментов'],
            datasets: [
              {
                label: 'Весна',
                data: [65, 80, 70, 90, 75, 75, 75, 98],
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgb(54, 162, 235)'
              },
              {
                label: 'Осень',
                data: [50, 75, 85, 60, 34, 56, 67, 95],
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgb(255, 99, 132)'
              }
            ]
          }
        },
        {
          name: 'Температура почвы',
          datasets: [
            {
              label: 'Диаграмма рассеяния между содержанием органического вещества и уровнем pH.',
              backgroundColor: '#f87979',
              data: [40, 39, 10, 40, 39, 80, 40],
              fill: false,
              borderColor: '#f87979',
              tension: 0.1
            },
            {
              label: 'Карта распределения pH по полю.',
              backgroundColor: '#da7827',
              data: [39, 20, 5, 67, 4, 56, 0],
              fill: false,
              borderColor: '#da7827',
              tension: 0.1
            }
          ],
          polarAnalyzes: {
            title: 'Исследование',
            labels: [
              'Оксиды железа',
              'Глины',
              'Карбонаты',
              'Сульфиды',
              'Фосфориты',
              'Силикаты',
              'Соли'
            ],
            datasets: [
              {
                label: 'Типы минералов',
                data: [65, 59, 90, 81, 56, 55, 40],
                backgroundColor: [
                  'rgb(255, 99, 132)',
                  'rgb(75, 192, 192)',
                  'rgb(255, 205, 86)',
                  'rgb(201, 203, 207)',
                  'rgb(54, 162, 235)',
                  'rgb(153, 102, 255)',
                  'rgb(255, 159, 64)'
                ],
                borderColor: [
                  'rgba(255, 255, 255, 1)',
                ],
                borderWidth: 2
              }
            ]
          },
          barAnalyzes: {
            title: 'Исследование',
            labels: [
              'Арбуз',
              'Дыня',
              'Помидоры',
              'Картофель',
              'Морковь',
              'Лук',
              'Кукуруза',
              'Пшеница',
              'Рис',
              'Ячмень',
              'Овес',
              'Хлопок'
            ],
            datasets: [
              {
                label: 'Результаты урожая за период',
                data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 99],
                backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(255, 159, 64, 0.2)',
                  'rgba(255, 205, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(102, 255, 102, 0.2)',
                  'rgba(255, 128, 0, 0.2)',
                  'rgba(128, 0, 255, 0.2)',
                  'rgba(255, 128, 192, 0.2)',
                  'rgba(255, 51, 153, 0.2)'
                ],
                borderColor: [
                  'rgb(255, 99, 132)',
                  'rgb(255, 159, 64)',
                  'rgb(255, 205, 86)',
                  'rgb(75, 192, 192)',
                  'rgb(54, 162, 235)',
                  'rgb(153, 102, 255)',
                  'rgb(255, 206, 86)',
                  'rgb(102, 255, 102)',
                  'rgb(255, 128, 0)',
                  'rgb(128, 0, 255)',
                  'rgb(255, 128, 192)',
                  'rgb(255, 51, 153)'
                ],
                borderWidth: 1
              }
            ]
          },
          radarAnalyzes: {
            title: 'Исследование',
            labels: ['Температура почвы', 'Влажность', 'Питательные вещества', 'Кислотность', 'Плотность почвы', 'Солнечное излучение', 'Частота осадков', 'Активность ферментов'],
            datasets: [
              {
                label: 'Весна',
                data: [65, 80, 70, 90, 75, 75, 75, 98],
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgb(54, 162, 235)'
              },
              {
                label: 'Осень',
                data: [50, 75, 85, 60, 34, 56, 67, 95],
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgb(255, 99, 132)'
              }
            ]
          }
        },
        {
          name: 'Уровень грунтовых вод',
          datasets: [
            {
              label: 'Диаграмма рассеяния между содержанием органического вещества и уровнем pH.',
              backgroundColor: '#f87979',
              data: [40, 39, 10, 40, 39, 80, 40],
              fill: false,
              borderColor: '#f87979',
              tension: 0.1
            },
            {
              label: 'Карта распределения pH по полю.',
              backgroundColor: '#da7827',
              data: [39, 20, 5, 67, 4, 56, 0],
              fill: false,
              borderColor: '#da7827',
              tension: 0.1
            }
          ],
          polarAnalyzes: {
            title: 'Исследование',
            labels: [
              'Оксиды железа',
              'Глины',
              'Карбонаты',
              'Сульфиды',
              'Фосфориты',
              'Силикаты',
              'Соли'
            ],
            datasets: [
              {
                label: 'Типы минералов',
                data: [65, 59, 90, 81, 56, 55, 40],
                backgroundColor: [
                  'rgb(255, 99, 132)',
                  'rgb(75, 192, 192)',
                  'rgb(255, 205, 86)',
                  'rgb(201, 203, 207)',
                  'rgb(54, 162, 235)',
                  'rgb(153, 102, 255)',
                  'rgb(255, 159, 64)'
                ],
                borderColor: [
                  'rgba(255, 255, 255, 1)',
                ],
                borderWidth: 2
              }
            ]
          },
          barAnalyzes: {
            title: 'Исследование',
            labels: [
              'Арбуз',
              'Дыня',
              'Помидоры',
              'Картофель',
              'Морковь',
              'Лук',
              'Кукуруза',
              'Пшеница',
              'Рис',
              'Ячмень',
              'Овес',
              'Хлопок'
            ],
            datasets: [
              {
                label: 'Результаты урожая за период',
                data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 99],
                backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(255, 159, 64, 0.2)',
                  'rgba(255, 205, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(102, 255, 102, 0.2)',
                  'rgba(255, 128, 0, 0.2)',
                  'rgba(128, 0, 255, 0.2)',
                  'rgba(255, 128, 192, 0.2)',
                  'rgba(255, 51, 153, 0.2)'
                ],
                borderColor: [
                  'rgb(255, 99, 132)',
                  'rgb(255, 159, 64)',
                  'rgb(255, 205, 86)',
                  'rgb(75, 192, 192)',
                  'rgb(54, 162, 235)',
                  'rgb(153, 102, 255)',
                  'rgb(255, 206, 86)',
                  'rgb(102, 255, 102)',
                  'rgb(255, 128, 0)',
                  'rgb(128, 0, 255)',
                  'rgb(255, 128, 192)',
                  'rgb(255, 51, 153)'
                ],
                borderWidth: 1
              }
            ]
          },
          radarAnalyzes: {
            title: 'Исследование',
            labels: ['Температура почвы', 'Влажность', 'Питательные вещества', 'Кислотность', 'Плотность почвы', 'Солнечное излучение', 'Частота осадков', 'Активность ферментов'],
            datasets: [
              {
                label: 'Весна',
                data: [65, 80, 70, 90, 75, 75, 75, 98],
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgb(54, 162, 235)'
              },
              {
                label: 'Осень',
                data: [50, 75, 85, 60, 34, 56, 67, 95],
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgb(255, 99, 132)'
              }
            ]
          }
        },
        {
          name: 'Наличие вредителей',
          datasets: [
            {
              label: 'Диаграмма рассеяния между содержанием органического вещества и уровнем pH.',
              backgroundColor: '#f87979',
              data: [40, 39, 10, 40, 39, 80, 40],
              fill: false,
              borderColor: '#f87979',
              tension: 0.1
            },
            {
              label: 'Карта распределения pH по полю.',
              backgroundColor: '#da7827',
              data: [39, 20, 5, 67, 4, 56, 0],
              fill: false,
              borderColor: '#da7827',
              tension: 0.1
            }
          ],
          polarAnalyzes: {
            title: 'Исследование',
            labels: [
              'Оксиды железа',
              'Глины',
              'Карбонаты',
              'Сульфиды',
              'Фосфориты',
              'Силикаты',
              'Соли'
            ],
            datasets: [
              {
                label: 'Типы минералов',
                data: [65, 59, 90, 81, 56, 55, 40],
                backgroundColor: [
                  'rgb(255, 99, 132)',
                  'rgb(75, 192, 192)',
                  'rgb(255, 205, 86)',
                  'rgb(201, 203, 207)',
                  'rgb(54, 162, 235)',
                  'rgb(153, 102, 255)',
                  'rgb(255, 159, 64)'
                ],
                borderColor: [
                  'rgba(255, 255, 255, 1)',
                ],
                borderWidth: 2
              }
            ]
          },
          barAnalyzes: {
            title: 'Исследование',
            labels: [
              'Арбуз',
              'Дыня',
              'Помидоры',
              'Картофель',
              'Морковь',
              'Лук',
              'Кукуруза',
              'Пшеница',
              'Рис',
              'Ячмень',
              'Овес',
              'Хлопок'
            ],
            datasets: [
              {
                label: 'Результаты урожая за период',
                data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 99],
                backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(255, 159, 64, 0.2)',
                  'rgba(255, 205, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(102, 255, 102, 0.2)',
                  'rgba(255, 128, 0, 0.2)',
                  'rgba(128, 0, 255, 0.2)',
                  'rgba(255, 128, 192, 0.2)',
                  'rgba(255, 51, 153, 0.2)'
                ],
                borderColor: [
                  'rgb(255, 99, 132)',
                  'rgb(255, 159, 64)',
                  'rgb(255, 205, 86)',
                  'rgb(75, 192, 192)',
                  'rgb(54, 162, 235)',
                  'rgb(153, 102, 255)',
                  'rgb(255, 206, 86)',
                  'rgb(102, 255, 102)',
                  'rgb(255, 128, 0)',
                  'rgb(128, 0, 255)',
                  'rgb(255, 128, 192)',
                  'rgb(255, 51, 153)'
                ],
                borderWidth: 1
              }
            ]
          },
          radarAnalyzes: {
            title: 'Исследование',
            labels: ['Температура почвы', 'Влажность', 'Питательные вещества', 'Кислотность', 'Плотность почвы', 'Солнечное излучение', 'Частота осадков', 'Активность ферментов'],
            datasets: [
              {
                label: 'Весна',
                data: [65, 80, 70, 90, 75, 75, 75, 98],
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgb(54, 162, 235)'
              },
              {
                label: 'Осень',
                data: [50, 75, 85, 60, 34, 56, 67, 95],
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgb(255, 99, 132)'
              }
            ]
          }
        },
        {
          name: 'Наличие болезней',
          datasets: [
            {
              label: 'Диаграмма рассеяния между содержанием органического вещества и уровнем pH.',
              backgroundColor: '#f87979',
              data: [40, 39, 10, 40, 39, 80, 40],
              fill: false,
              borderColor: '#f87979',
              tension: 0.1
            },
            {
              label: 'Карта распределения pH по полю.',
              backgroundColor: '#da7827',
              data: [39, 20, 5, 67, 4, 56, 0],
              fill: false,
              borderColor: '#da7827',
              tension: 0.1
            }
          ],
          polarAnalyzes: {
            title: 'Исследование',
            labels: [
              'Оксиды железа',
              'Глины',
              'Карбонаты',
              'Сульфиды',
              'Фосфориты',
              'Силикаты',
              'Соли'
            ],
            datasets: [
              {
                label: 'Типы минералов',
                data: [65, 59, 90, 81, 56, 55, 40],
                backgroundColor: [
                  'rgb(255, 99, 132)',
                  'rgb(75, 192, 192)',
                  'rgb(255, 205, 86)',
                  'rgb(201, 203, 207)',
                  'rgb(54, 162, 235)',
                  'rgb(153, 102, 255)',
                  'rgb(255, 159, 64)'
                ],
                borderColor: [
                  'rgba(255, 255, 255, 1)',
                ],
                borderWidth: 2
              }
            ]
          },
          barAnalyzes: {
            title: 'Исследование',
            labels: [
              'Арбуз',
              'Дыня',
              'Помидоры',
              'Картофель',
              'Морковь',
              'Лук',
              'Кукуруза',
              'Пшеница',
              'Рис',
              'Ячмень',
              'Овес',
              'Хлопок'
            ],
            datasets: [
              {
                label: 'Результаты урожая за период',
                data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 99],
                backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(255, 159, 64, 0.2)',
                  'rgba(255, 205, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(102, 255, 102, 0.2)',
                  'rgba(255, 128, 0, 0.2)',
                  'rgba(128, 0, 255, 0.2)',
                  'rgba(255, 128, 192, 0.2)',
                  'rgba(255, 51, 153, 0.2)'
                ],
                borderColor: [
                  'rgb(255, 99, 132)',
                  'rgb(255, 159, 64)',
                  'rgb(255, 205, 86)',
                  'rgb(75, 192, 192)',
                  'rgb(54, 162, 235)',
                  'rgb(153, 102, 255)',
                  'rgb(255, 206, 86)',
                  'rgb(102, 255, 102)',
                  'rgb(255, 128, 0)',
                  'rgb(128, 0, 255)',
                  'rgb(255, 128, 192)',
                  'rgb(255, 51, 153)'
                ],
                borderWidth: 1
              }
            ]
          },
          radarAnalyzes: {
            title: 'Исследование',
            labels: ['Температура почвы', 'Влажность', 'Питательные вещества', 'Кислотность', 'Плотность почвы', 'Солнечное излучение', 'Частота осадков', 'Активность ферментов'],
            datasets: [
              {
                label: 'Весна',
                data: [65, 80, 70, 90, 75, 75, 75, 98],
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgb(54, 162, 235)'
              },
              {
                label: 'Осень',
                data: [50, 75, 85, 60, 34, 56, 67, 95],
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgb(255, 99, 132)'
              }
            ]
          }
        },
      ],
      showFilters: false,
      showAnalyzes: false,
      months: [
        {
          name: 'Январь',
          en_name: 'January'
        },
        {
          name: 'Февраль',
          en_name: 'February'
        },
        {
          name: 'Март',
          en_name: 'March'
        },
        {
          name: 'Апрель',
          en_name: 'April'
        },
        {
          name: 'Май',
          en_name: 'May'
        },
        {
          name: 'Июнь',
          en_name: 'June'
        },
        {
          name: 'Июль',
          en_name: 'July'
        },
        {
          name: 'Августь',
          en_name: 'August'
        },
        {
          name: 'Сентябрь',
          en_name: 'September'
        },
        {
          name: 'Октябрь',
          en_name: 'October'
        },
        {
          name: 'Ноябрь',
          en_name: 'November'
        },
        {
          name: 'Декабр',
          en_name: 'December'
        }
      ],
      districsInfo: [],
      showDistrictFilter: false,
      activeDistrictFilter: {},
      districsArray: [],
      activeLight: true,
      activeGaz: false,
      totalData: {},
      totalMarks: {},
      showRightSide: false
    }
  },
  computed: {
    getFillColor() {
      return (id) => {
        const district = this.districts.find(d => d.district_id === id);
        return district ? district.fill : '#D7D7D7';
      };
    },
    getIndexText() {
      if (this.activeDistrict.index <= 25) {
        return 'Баланд'
      } else if (this.activeDistrict.index <= 60) {
        return 'Ўртача'
      } else {
        return 'Паст'
      }
    },
    getIndexNumber() {
      if (this.activeDistrict.index <= 25) {
        return 9
      } else if (this.activeDistrict.index <= 60) {
        return 4
      } else {
        return 3
      }
    },
  },
  methods: {
    getDistrictData(id) {
      return this.districts.find(district => district.district_id === id);
    },
    changeActiveAnalyzes(item) {
      this.showAnalyzes = false
      this.activeAnalyze = item;
    },
    changeShowAnalyzes() {
      this.showAnalyzes = !this.showAnalyzes;
    },
    changeShowDistrictFilter() {
      this.showDistrictFilter = !this.showDistrictFilter;
    },
    changeActiveDistrictFilter(item) {
      this.activeDistrictFilter = item
      this.showDistrictFilter = false
    },
    setActiveDistrict(id) {
      if (id === this.activeDistrict.id) {
        this.activeDistrict = {};
      } else {
        const district = this.districsArray.find(d => d.id === id);
        const districtNames = this.districsArray.find(d => d.id === id);
        if (district) {
          this.activeDistrict = district;
          this.activeDistrictFilter = districtNames
          this.showRightSide = false
        }
      }

      if(this.dates.from && this.dates.to && this.activeDistrict.id && typeof this.activeDistrict.id === "number"){
        axios.get(`general/district/${id}?start_date=${this.formatDate(this.dates.from)}&end_date=${this.formatDate(this.dates.to)}`).then(res=> {

        }).catch(err=> {
          console.log(err)
        })
      }
    },
    formatDate(date, options = {}) {
      const year = date.getFullYear();
      let month = date.getMonth() + 1;
      let day = date.getDate();

      if (options.month) month = options.month;
      if (options.day) day = options.day;

      month = month.toString().padStart(2, '0');
      day = day.toString().padStart(2, '0');

      return `${year}-${month}-${day}`;
    },
    resetActiveDistrict() {
      this.activeDistrictFilter = {}
      this.activeDistrict = {};
      this.showRightSide = true
    },
    handleClickOutside(event) {
      if (!event.target.closest('.district') && !event.target.closest('.menu') && !event.target.closest('.districs-filters-list') && !event.target.closest('.districs-filters')) {
        this.resetActiveDistrict();
      }
      if (!event.target.closest('.filters-list') && !event.target.closest('.filters')) {
        this.showFilters = false
      }
      if (!event.target.closest('.districs-filters-list') && !event.target.closest('.districs-filters')) {
        this.showDistrictFilter = false
      }
    },
    getMonthName(monthNumber) {
      const monthNames = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
      ];

      if (monthNumber < 0 || monthNumber > 11) {
        throw new Error("Month number must be between 0 and 11");
      }

      return monthNames[monthNumber];
    },
    getIndicatorStyle() {
      if (this.activeDistrict && this.activeDistrict.id) {

      } else {
        const MAX = 97.5;

        let result;
        if (this.activeLight) {
          result = MAX - this.totalMarks.light_mark;
        } else {
          result = MAX - this.totalMarks.gas_mark;
        }

        if (result < 4)
          result = 4;
        else if (result > 96)
          result = 100;

        return {
          left: `${result}%`
        };
      }
    },
    getColorByKey(districtId, key) {
      const district = this.districts.find((item) => item.district_id === districtId);
      if (!district) return null;

      const gasValue = district.gas_variables.find((variable) =>
          Object.keys(variable).includes(key)
      );

      const lightValue = district.light_variables.find((variable) =>
          Object.keys(variable).includes(key)
      );

      const value = gasValue ? gasValue[key] : lightValue ? lightValue[key] : null;
      if (value === null) return null;


      if (value <= 25) return '#FF0000';
      else if (value <= 60) return '#FFDE30';
      else return '#509948';
    },
    getColorClass(districtId, key) {
      const color = this.getColorByKey(districtId, key);

      return {
        'text-[#FF0000]': color === '#FF0000',
        'text-[#FFDE30]': color === '#FFDE30',
        'text-[#509948]': color === '#509948',
      };
    },
    formatNumber(value) {
      if (!Number.isFinite(value)) return value;

      const [integerPart, decimalPart] = value.toLocaleString('ru-RU').split(',');

      if (!decimalPart) {
        return integerPart;
      }

      return `${integerPart}.${decimalPart}`;
    },
    animateDistrics(){
      const districts = {
        'okrug-1': { animation: 'fadeInDown', duration: '1.1s' },
        'okrug-2': { animation: 'fadeInDown', duration: '2s' },
        'okrug-3': { animation: 'fadeInDown', duration: '2s' },
        'okrug-4': { animation: 'fadeInLeft', duration: '2s' },
        'okrug-5': { animation: 'fadeInDown', duration: '1.5s' },
        'okrug-6': { animation: 'fadeInRight', duration: '2s' },
        'okrug-7': { animation: 'fadeInLeft', duration: '1.3s' },
        'okrug-8': { animation: 'fadeInRight', duration: '1.5s' },
        'okrug-9': { animation: 'fadeInDown', duration: '1.5s' },
        'okrug-10': { animation: 'fadeInLeft', duration: '1.7s' },
        'okrug-11': { animation: 'fadeInDown', duration: '1.7s' },
        'okrug-12': { animation: 'fadeInDown', duration: '1s' },
        'okrug-13': { animation: 'fadeInDown', duration: '1.2s' },
        'okrug-14': { animation: 'fadeInRight', duration: '1.8s' },
        'okrug-15': { animation: 'fadeInDown', duration: '2.2s' }
      };

      Object.keys(districts).forEach(key => {
        const district = document.getElementById(key);
        if (district) {
          const { animation, duration } = districts[key];
          district.style.animation = animation;
          district.style.animationDuration = duration;
        }
      });
    }
  },
  mounted() {
    const that = this;
    document.addEventListener('click', this.handleClickOutside);
    this.animateDistrics()
    const tooltip = document.getElementById('tooltip');
    const districtName = document.getElementById('district-name');

    const elements = document.querySelectorAll('.district');

    elements.forEach((element) => {
      element.addEventListener('mouseover', function (event) {
        const id = element.getAttribute('data-id');
        element.parentNode.appendChild(element)
        element.style.animation = '';
        element.style.animationDuration = '';
        // данные
        const districtData = that.getDistrictData(id);

        if (districtData && districtData.name) {
          districtName.textContent = districtData.name
        }

        // расположение
        const rect = element.getBoundingClientRect();
        const tooltipRect = tooltip.getBoundingClientRect();

        // посередине
        // const centerX = rect.left + (rect.width / 2);
        // const centerY = rect.top + (rect.height / 2);
        const screenWidth = window.innerWidth;
        let centerX;
        let centerY;
        if (screenWidth > 1370) {
          // справа
          const offsetX = 50;
          const offsetY = 10;
          centerX = rect.right + offsetX;
          centerY = rect.top - offsetY
        } else {
          const offsetX = -96;
          const offsetY = 10;
          const tooltipWidth = tooltipRect.width;

          centerX = rect.left - tooltipWidth - offsetX;
          centerY = rect.top + (rect.height / 2) - (tooltipRect.height / 2);
        }
        tooltip.style.left = `${centerX}px`;
        tooltip.style.top = `${centerY}px`;
        tooltip.style.transform = 'translate(-50%, -100%)';

        tooltip.classList.add('show');
      });

      element.addEventListener('mouseout', function () {
        element.style.fill = '';
        tooltip.classList.remove('show');

      });
    });
    const currentMonthNumber = new Date().getMonth();
    const previousMonthNumber = (currentMonthNumber - 1 + 12) % 12;

    this.activeFilter = this.months.find(month => month.en_name === this.getMonthName(previousMonthNumber));

    axios.get('general/country?lang=en&page=1&limit=15').then(districs => {
      this.districsArray = districs.data.data[0].regions

    }).catch(error => {
      console.error('eror')
    })
  },
  watch: {
    dates: {
      handler(newVal, oldVal) {
        if(this.dates.from && this.dates.to && this.activeDistrict.id && typeof this.activeDistrict.id ==="number"){
          axios.get(`general/district/${this.activeDistrict.id}?start_date=${this.formatDate(this.dates.from)}&end_date=${this.formatDate(this.dates.to)}`).then(res=> {

          }).catch(err=> {
            console.log(err)
          })
        }
      },
      deep: true
    }
  }
}
</script>

<template>
  <AdminHeader/>
  <section class="py-3 bg-white">
    <div class="px-3">
      <div class="flex flex-col gap-5 items-center justify-between w-full relative max_lg:flex-col max_lg:gap-5">
        <MainTitle>
          Интерактивная карта потребителей Ташкентской области
        </MainTitle>
        <div class="relative flex items-center gap-3 max_md2:flex-col">
          <!--start districs filter-->
          <DistricsFilter
              v-if="districsArray.length"
              :active-district-filter="activeDistrictFilter"
              :show-district-filter="showDistrictFilter"
              :districs-array="districsArray"
              @changeShowDistrictFilter="changeShowDistrictFilter"
              @changeActiveDistrictFilter="changeActiveDistrictFilter"
              @setActiveDistrict="setActiveDistrict"
          />
          <!--end districs filter-->

          <!--start types filter-->
          <TypesFilter
              :analyzes="analyzes"
              :active-analyze="activeAnalyze"
              :show-analyzes="showAnalyzes"
              :active-filter="activeFilter"
              @changeActiveAnalyzes="changeActiveAnalyzes"
              @changeShowAnalyzes="changeShowAnalyzes"
          />
          <!--end types filter-->

          <!--start period filters-->
          <date-picker
              v-model="dates.from"
              placeholder="От"
          />
          <date-picker
              v-model="dates.to"
              placeholder="До"
          />
          <!--end period filter-->
        </div>
      </div>

      <div class="border mt-2 p-2 rounded-[30px] w-full">
        <div
            class="rounded-[27px] max_big:pr-32 max_md:pr-0 bg-romance w-full min-h-[82vh] max-h-[660px] flex justify-between p-[18px] relative z-[100]">
          <!--          start left side-->
          <Transition name="left-fade-fast">
            <div v-if="activeDistrict && activeDistrict.id"
                 class="max_big:hidden w-[32%] max_lg:w-[50%] max_md:w-full max_md:max-h-full max_big:absolute max_big:top-0 max_big:right-0 left-menu mt-[35px] bg-white h-full max-h-[540px] rounded-[27px] overflow-y-auto overflow-x-hidden py-[30px] px-5"
            >
              Информация дополнительная
            </div>
          </Transition>
          <!--          end left side-->

          <!--        start map-->
          <Transition name="left-fade-fast">
            <SvgMap
                :get-fill-color="getFillColor"
                :active-district="activeDistrict"
                @setActiveDistrict="setActiveDistrict"
            />
          </Transition>
          <!--          end map-->

          <Tooltip>
            [Сарлавҳа района/города]
          </Tooltip>

          <!--          start right side-->
          <Transition name="left-fade-fast">
            <div v-if="activeDistrict && activeDistrict.id"
                 class="max_big:absolute max_big:top-4 max_big:right-0 menu mt-[35px] bg-white h-full max-h-[540px] w-[32%] max_lg:w-[50%] max_md:w-full max_md:max-h-full rounded-[27px] overflow-y-auto py-[30px] px-5"
            >
              <div @click="activeDistrict={}; showRightSide = true" class="hidden max_lg:block absolute top-2 right-3">
                <img class="w-[32px] h-[32px]" src="/img/close.svg" alt="close">
              </div>
              <p>
                Информация основная
              </p>
            </div>
          </Transition>
          <!--          end right side-->
        </div>
      </div>

      <ChartsStatistic
          v-if="activeAnalyze.name"
          :activeAnalyze="activeAnalyze"
      />
    </div>
  </section>
</template>

<style>
h1 {
  animation: fadeInDown;
  animation-duration: 2s;
}

.filters {
  animation: fadeInRight;
  animation-duration: 2s;
}

.districs-filters {
  animation: fadeInRight;
  animation-duration: 2s;
}

.click-button {
  animation: fadeInRight;
  animation-duration: 1.5s;
}

.indicators {
  animation: fadeInRight;
  animation-duration: 1.5s;
}

.menu {
  animation: fadeInRight;
  animation-duration: 1.2s;
}

.left-menu {
  animation: fadeInLeft;
  animation-duration: 1.2s;
}

</style>