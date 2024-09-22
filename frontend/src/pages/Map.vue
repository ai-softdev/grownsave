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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
            title: 'Исследование чего-то',
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
          name: 'Феврал',
          en_name: 'February'
        },
        {
          name: 'Март',
          en_name: 'March'
        },
        {
          name: 'Апрел',
          en_name: 'April'
        },
        {
          name: 'Май',
          en_name: 'May'
        },
        {
          name: 'Июн',
          en_name: 'June'
        },
        {
          name: 'Июл',
          en_name: 'July'
        },
        {
          name: 'Август',
          en_name: 'August'
        },
        {
          name: 'Сентябр',
          en_name: 'September'
        },
        {
          name: 'Октябр',
          en_name: 'October'
        },
        {
          name: 'Ноябр',
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

      // axios.get(`district/${item.en_name}`).then(res => {
      //   this.districsInfo = res.data;
      //   this.districts = []
      //   this.calculateStandart()
      // })
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

      if(this.dates.from && this.dates.to){
        const dateFrom = new Date(this.dates.from);
        dateFrom.setMonth(3);
        dateFrom.setDate(20);
        const formattedFrom = dateFrom.toISOString().split('T')[0];

        const dateTo = new Date(this.dates.from);
        dateTo.setMonth(3);
        dateTo.setDate(20);
        const formattedTo = dateTo.toISOString().split('T')[0];
        axios.get(`general/district/${id}?start_date=${formattedFrom}&end_date=${formattedTo}`).then(res=> {

        }).catch(err=> {
          console.log(err)
        })
      }
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
      console.log(this.totalMarks)
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
    }
  },
  mounted() {
    const that = this;
    document.addEventListener('click', this.handleClickOutside);
    const tooltip = document.getElementById('tooltip');
    const districtName = document.getElementById('district-name');

    const elements = document.querySelectorAll('.district');

    const bostanlik = document.getElementById('okrug-2');
    const kibray = document.getElementById('okrug-5');
    const zangiota = document.getElementById('okrug-11');
    const yangiyul = document.getElementById('okrug-13');
    const chinaz = document.getElementById('okrug-4');
    const ukorichirchik = document.getElementById('okrug-14');
    const urtachirchik = document.getElementById('okrug-12');
    const quyichirchik = document.getElementById('okrug-10');
    const pskent = document.getElementById('okrug-9');
    const parkent = document.getElementById('okrug-8');
    const aqqurganskiy = document.getElementById('okrug-7');
    const axangaran = document.getElementById('okrug-6');
    const bukinskiy = document.getElementById('okrug-3');
    const bekabad = document.getElementById('okrug-1');
    const tashkent = document.getElementById('okrug-15');
    tashkent.style.animation = 'fadeInDown';
    tashkent.style.animationDuration = '2.2s';
    bostanlik.style.animation = 'fadeInDown';
    bostanlik.style.animationDuration = '2s';
    kibray.style.animation = 'fadeInDown';
    kibray.style.animationDuration = '1.5s';
    zangiota.style.animation = 'fadeInDown';
    zangiota.style.animationDuration = '1.7s';
    yangiyul.style.animation = 'fadeInDown';
    yangiyul.style.animationDuration = '1.2s';
    chinaz.style.animation = 'fadeInLeft';
    chinaz.style.animationDuration = '2s';
    quyichirchik.style.animation = 'fadeInLeft';
    quyichirchik.style.animationDuration = '1.7s';
    aqqurganskiy.style.animation = 'fadeInLeft';
    aqqurganskiy.style.animationDuration = '1.3s';
    bukinskiy.style.animation = 'fadeInDown';
    bukinskiy.style.animationDuration = '2s';
    pskent.style.animation = 'fadeInDown';
    pskent.style.animationDuration = '1.5s';
    bekabad.style.animation = 'fadeInDown';
    bekabad.style.animationDuration = '1.1s';
    urtachirchik.style.animation = 'fadeInDown';
    urtachirchik.style.animationDuration = '1s';
    axangaran.style.animation = 'fadeInRight';
    axangaran.style.animationDuration = '2s';
    ukorichirchik.style.animation = 'fadeInRight';
    ukorichirchik.style.animationDuration = '1.8s';
    parkent.style.animation = 'fadeInRight';
    parkent.style.animationDuration = '1.5s';

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
              Информация
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

          <!--          start menu-->
          <Transition name="left-fade-fast">
            <div v-if="activeDistrict && activeDistrict.district_id"
                 class="max_big:absolute max_big:top-4 max_big:right-0 menu mt-[35px] bg-white h-full max-h-[540px] w-[32%] max_lg:w-[50%] max_md:w-full max_md:max-h-full rounded-[27px] overflow-y-auto py-[30px] px-5"
            >
              <div @click="activeDistrict={}; showRightSide = true" class="hidden max_lg:block absolute top-2 right-3">
                <img class="w-[32px] h-[32px]" src="/img/close.svg" alt="close">
              </div>
              <div class="flex items-center gap-4 mb-10">
                <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path
                      class="transition-all ease-in-out duration-300"
                      d="M18.9993 2.66666H11.3253C11.086 2.66666 10.9663 2.66666 10.8607 2.7031C10.7673 2.73531 10.6822 2.7879 10.6116 2.85704C10.5317 2.93523 10.4782 3.04226 10.3712 3.2563L4.77122 14.4563C4.51564 14.9675 4.38786 15.2231 4.41855 15.4308C4.44535 15.6121 4.5457 15.7745 4.69596 15.8796C4.86806 16 5.15379 16 5.72527 16H13.9993L9.99938 29.3333L26.2568 12.4737C26.8053 11.9049 27.0796 11.6205 27.0956 11.3772C27.1095 11.1659 27.0223 10.9606 26.8605 10.824C26.6743 10.6667 26.2792 10.6667 25.4889 10.6667H15.9993L18.9993 2.66666Z"
                      :stroke="activeDistrict.index <= 25 ? '#D80000' : activeDistrict.index <= 60 ? '#FFDE30' : '#30B502'"
                      stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <div
                    class="font-bold text-[27px] transition-all ease-in-out duration-300"
                    :class="{
                      'text-[#D80000]': activeDistrict.index <= 25,
                      'text-[#FFDE30]': activeDistrict.index > 25 && activeDistrict.index <= 60,
                      'text-positive': activeDistrict.index > 60
                    }"
                >
                  {{ getIndexNumber }} - {{ getIndexText }}!
                </div>
              </div>
              <div class="relative pb-12">
                <img class="w-full" src="/img/indicator.svg" alt="indicator">
                <!--                :class="{-->
                <!--                'left-[20%]': activeDistrict.index > 60,-->
                <!--                'left-[35%]': activeDistrict.index > 25 && activeDistrict.index <= 60,-->
                <!--                'left-[80%]': activeDistrict.index <= 25-->
                <!--                }"-->
                <svg
                    class="absolute bottom-4 transition-all ease-in-out duration-300"
                    :style="getIndicatorStyle()"
                    width="18" height="18" viewBox="0 0 18 18" fill="none"
                    xmlns="http://www.w3.org/2000/svg">
                  <path
                      class="transition-all ease-in-out duration-300"
                      d="M15.8801 17.397C16.486 17.6635 16.789 17.7968 16.9701 17.7381C17.127 17.6873 17.2488 17.5623 17.2956 17.4041C17.3495 17.2214 17.2083 16.9221 16.9259 16.3234L9.72355 1.05437C9.49252 0.564589 9.377 0.319697 9.21839 0.242686C9.0805 0.17573 8.91951 0.175723 8.78161 0.242686C8.62301 0.31969 8.50749 0.564589 8.27645 1.05437L1.07401 16.3234C0.791622 16.9221 0.650426 17.2214 0.704357 17.4041C0.751111 17.5622 0.872839 17.6872 1.02982 17.7381C1.21098 17.7968 1.5139 17.6635 2.11982 17.397L8.67781 14.5114C8.79647 14.4592 8.85579 14.4331 8.91745 14.4228C8.97211 14.4137 9.02783 14.4137 9.08249 14.4228C9.14415 14.4331 9.20348 14.4592 9.32213 14.5114L15.8801 17.397Z"
                      :fill="activeDistrict.index <= 25 ? '#D80000' : activeDistrict.index <= 60 ? '#FFDE30' : '#30B502'"
                  />
                </svg>
              </div>
              <div>
                <div class="flex items-center gap-2 mb-6">
                  <img src="/img/info.svg" alt="info">
                  <p class="font-medium text-lg">
                    Умумий маълумот
                  </p>
                </div>
                <div class="flex items-center gap-2 justify-between border-b pb-5 text-stormDust">
                  <p>Сарлавҳа:</p>
                  <p>{{ activeDistrict.name }}</p>
                </div>
                <div class="flex items-center gap-2 justify-between border-b pb-5 text-stormDust mt-5">
                  <p>Аҳолиси:</p>
                  <p>{{ formatNumber(activeDistrict.population) }}</p>
                </div>
                <div class="flex items-center gap-2 justify-between border-b pb-5 text-stormDust mt-5">
                  <p>ҳудуд:</p>
                  <p>{{ formatNumber(activeDistrict.area) }} кв/км</p>
                </div>
                <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                  <p class="font-medium text-lg">
                    Юридик шахслар сони:
                  </p>
                  <p class="ml-auto">{{ formatNumber(activeDistrict.data.count_legal_entities) }}</p>
                </div>
                <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                  <p class="font-medium text-lg">
                    Ахоли истеъмолчилар сони:
                  </p>
                  <p class="ml-auto">{{ formatNumber(activeDistrict.data.count_consumers) }}</p>
                </div>
                <div v-if="activeLight">
                  <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                    <p class="font-medium text-lg">
                      Вилоятда нечта ПС оркали элект энергияси билан таьминланади
                    </p>
                    <p class="ml-auto">{{ formatNumber(activeDistrict.data.light.count_PS) }}</p>
                  </div>
                  <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                    <p class="font-medium text-lg">
                      Вилоятдаги истеъмолчиларда нечта ПС мавжуд
                    </p>
                    <p class="ml-auto">{{ formatNumber(activeDistrict.data.light.count_PS2) }}</p>
                  </div>
                  <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                    <p class="font-medium text-lg">
                      ТЭТ балансида канча 35/10/6/0,4 кВли электр узатиш тармоғи (км) мавжуд хар бирини алохида алохида
                      узунлиги курсатилган холда
                    </p>
                    <p class="ml-auto">{{ formatNumber(activeDistrict.data.light.count_network_transmission) }}</p>
                  </div>
                  <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                    <p class="font-medium text-lg">
                      Истемолчи балансида канча 220/110/35 кВли электр узатиш тармоғи (км) мавжуд хар бирини алохида
                      алохида узунлиги курсатилган холда
                    </p>
                    <p class="ml-auto">{{ formatNumber(activeDistrict.data.light.count_powers_lines) }}</p>
                  </div>
                  <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                    <p class="font-medium text-lg">
                      Истемолчи балансида трансформаторлар сони
                    </p>
                    <p class="ml-auto">{{
                        formatNumber(activeDistrict.data.light.count_transformer_consumer_balance)
                      }}</p>
                  </div>
                  <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                    <p class="font-medium text-lg">
                      ТЭТ балансида трансформаторлар сони
                    </p>
                    <p class="ml-auto">{{ formatNumber(activeDistrict.data.light.count_transformers_balance) }}</p>
                  </div>
                  <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                    <p class="font-medium text-lg">
                      Истемолчи балансида канча 35/10/6/0,4 кВли электр узатиш тармоғи (км) мавжуд хар бирини алохида
                      алохида узунлиги курсатилган холда
                    </p>
                    <p class="ml-auto">{{ formatNumber(activeDistrict.data.light.count_volume_transmission) }}</p>
                  </div>
                  <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                    <p class="font-medium text-lg">
                      Кунлик электр энергия истемоли -мил кВт*соат
                    </p>
                    <p class="ml-auto">{{ formatNumber(activeDistrict.data.light.daily_electricity_consumption) }}</p>
                  </div>
                  <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                    <p class="font-medium text-lg">
                      Соатлик элект энергия истемоли мил кВт*соат
                    </p>
                    <p class="ml-auto">{{ formatNumber(activeDistrict.data.light.hourly_electricity_consumption) }}</p>
                  </div>
                  <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                    <p class="font-medium text-lg">
                      “ҲЭТ” АЖ Тошкент вилояти филиали балансида канча 220/110/35 кВли электр узатиш тармоғи (км) мавжуд
                      хар бирини алохида алохида узунлиги курсатилган холда
                    </p>
                    <p class="ml-auto">{{ formatNumber(activeDistrict.data.light.power_in_branch_indicated) }}</p>
                  </div>
                  <div class="hidden max_big:block mt-5">
                    <info
                        name="Тарғибот-ташвиқот ишлари"
                        :class-color="getColorClass(activeDistrict.district_id, 'advertising_activities')"
                        :fill="getColorByKey(activeDistrict.district_id, 'advertising_activities')"
                        :actual="activeDistrict.data.light.advertising_activities_actual"
                        :monthly="activeDistrict.data.light.advertising_activities_monthly"
                    />
                    <info
                        name="Кўча ёритиш чироқларини энерго самарадорлигини ошириш"
                        :class-color="getColorClass(activeDistrict.district_id, 'energy_of_street_lighting_lamps_Increased_efficiency')"
                        :fill="getColorByKey(activeDistrict.district_id, 'energy_of_street_lighting_lamps_Increased_efficiency')"
                        :actual="activeDistrict.data.light.energy_of_street_lighting_lamps_Increased_efficiency_actual"
                        :monthly="activeDistrict.data.light.energy_of_street_lighting_lamps_Increased_efficiency_monthly"
                    />
                    <info
                        name="Кушимча генерация хисобига"
                        :class-color="getColorClass(activeDistrict.district_id, 'for_additional_generation')"
                        :fill="getColorByKey(activeDistrict.district_id, 'for_additional_generation')"
                        :actual="activeDistrict.data.light.for_additional_generation_actual"
                        :monthly="activeDistrict.data.light.for_additional_generation_monthly"
                    />
                    <info
                        name="Йирик истеъмолчилар хисобига"
                        :class-color="getColorClass(activeDistrict.district_id, 'for_large_consumers')"
                        :fill="getColorByKey(activeDistrict.district_id, 'for_large_consumers')"
                        :actual="activeDistrict.data.light.for_large_consumers_actual"
                        :monthly="activeDistrict.data.light.for_large_consumers_monthly"
                    />
                    <info
                        name="Бино-иншоатларни иссиқликни йўқотилишини ҳимоялаш"
                        :class-color="getColorClass(activeDistrict.district_id, 'heating_of_buildings_Loss_Protection')"
                        :fill="getColorByKey(activeDistrict.district_id, 'heating_of_buildings_Loss_Protection')"
                        :actual="activeDistrict.data.light.heating_of_buildings_Loss_Protection_actual"
                        :monthly="activeDistrict.data.light.heating_of_buildings_Loss_Protection_monthly"
                    />
                    <info
                        name="Ноқонуний ҳолатларни аниқлаш"
                        :class-color="getColorClass(activeDistrict.district_id, 'identification_illegal_situations')"
                        :fill="getColorByKey(activeDistrict.district_id, 'identification_illegal_situations')"
                        :actual="activeDistrict.data.light.identification_illegal_situations_actual"
                        :monthly="activeDistrict.data.light.identification_illegal_situations_monthly"
                    />
                    <info
                        name="Янги қурилаётган кўпқаватли уйларга куёш панелларини ўрнатиш"
                        :class-color="getColorClass(activeDistrict.district_id, 'in_apartment_buildings_solar_panels')"
                        :fill="getColorByKey(activeDistrict.district_id, 'in_apartment_buildings_solar_panels')"
                        :actual="activeDistrict.data.light.in_apartment_buildings_solar_panels_actual"
                        :monthly="activeDistrict.data.light.in_apartment_buildings_solar_panels_monthly"
                    />
                    <info
                        name="Гелиоколлектор ўрнатиш ҳисобига"
                        :class-color="getColorClass(activeDistrict.district_id, 'installing_solar_collector')"
                        :fill="getColorByKey(activeDistrict.district_id, 'installing_solar_collector')"
                        :actual="activeDistrict.data.light.installing_solar_collector_actual"
                        :monthly="activeDistrict.data.light.installing_solar_collector_monthly"
                    />
                    <info
                        name="Ташкилий тадбирлар"
                        :class-color="getColorClass(activeDistrict.district_id, 'organizational_events')"
                        :fill="getColorByKey(activeDistrict.district_id, 'organizational_events')"
                        :actual="activeDistrict.data.light.organizational_events_actual"
                        :monthly="activeDistrict.data.light.organizational_events_monthly"
                    />
                    <info
                        name="Реактив энергияни компенсацияқилиш"
                        :class-color="getColorClass(activeDistrict.district_id, 'reactive_energy_compensation')"
                        :fill="getColorByKey(activeDistrict.district_id, 'reactive_energy_compensation')"
                        :actual="activeDistrict.data.light.reactive_energy_compensation_actual"
                        :monthly="activeDistrict.data.light.reactive_energy_compensation_monthly"
                    />
                    <info
                        name="Таъмирлаш ишлари"
                        :class-color="getColorClass(activeDistrict.district_id, 'repair_work')"
                        :fill="getColorByKey(activeDistrict.district_id, 'repair_work')"
                        :actual="activeDistrict.data.light.repair_work_actual"
                        :monthly="activeDistrict.data.light.repair_work_monthly"
                    />
                    <info
                        name="Тадбиркорлик субъектларига қуёш Панелларини ўрнати"
                        :class-color="getColorClass(activeDistrict.district_id, 'solar_business_entities_installation')"
                        :fill="getColorByKey(activeDistrict.district_id, 'solar_business_entities_installation')"
                        :actual="activeDistrict.data.light.solar_business_entities_installation_actual"
                        :monthly="activeDistrict.data.light.solar_business_entities_installation_monthly"
                    />
                    <info
                        name="Эхтиёжманд оилаларга қуёш панеллари ўрнатиш"
                        :class-color="getColorClass(activeDistrict.district_id, 'solar_panels_families')"
                        :fill="getColorByKey(activeDistrict.district_id, 'solar_panels_families')"
                        :actual="activeDistrict.data.light.solar_panels_families_actual"
                        :monthly="activeDistrict.data.light.solar_panels_families_monthly"
                    />
                    <info
                        name="Ижтимоий соха объектларига қуёш панеллар ўрнатиш"
                        :class-color="getColorClass(activeDistrict.district_id, 'solar_panels_public')"
                        :fill="getColorByKey(activeDistrict.district_id, 'solar_panels_public')"
                        :actual="activeDistrict.data.light.solar_panels_public_actual"
                        :monthly="activeDistrict.data.light.solar_panels_public_monthly"
                    />
                    <info
                        name="Тп ларда ташкилий техник тадбирлар хисобига"
                        :class-color="getColorClass(activeDistrict.district_id, 'to_take_into_account_organizational')"
                        :fill="getColorByKey(activeDistrict.district_id, 'to_take_into_account_organizational')"
                        :actual="activeDistrict.data.light.to_take_into_account_organizational_actual"
                        :monthly="activeDistrict.data.light.to_take_into_account_organizational_monthly"
                    />
                    <info
                        name="Трансфрматорларда юкламаларни тенг тақсимлаш"
                        :class-color="getColorClass(activeDistrict.district_id, 'to_take_into_account_organizational')"
                        :fill="getColorByKey(activeDistrict.district_id, 'to_take_into_account_organizational')"
                        :actual="activeDistrict.data.light.uniform_distribution_loads_actual"
                        :monthly="activeDistrict.data.light.uniform_distribution_loads_monthly"
                    />
                  </div>
                </div>
                <div v-if="activeGaz">
                  <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                    <p class="font-medium text-lg">
                      АГҚШлар сони
                    </p>
                    <p class="ml-auto">{{ formatNumber(activeDistrict.data.gas.count_agqsh) }}</p>
                  </div>
                  <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                    <p class="font-medium text-lg">
                      АГТКШлар сони
                    </p>
                    <p class="ml-auto">{{ formatNumber(activeDistrict.data.gas.count_agtksh) }}</p>
                  </div>
                  <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                    <p class="font-medium text-lg">
                      Хар бир туманда мавжуд газ қувурлари юқори ўртиПаст
                    </p>
                    <p class="ml-auto">{{ formatNumber(activeDistrict.data.gas.count_gas_pipelines) }}</p>
                  </div>
                  <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                    <p class="font-medium text-lg">
                      ИЭСлар сони
                    </p>
                    <p class="ml-auto">{{ formatNumber(activeDistrict.data.gas.count_thermal_power) }}</p>
                  </div>
                  <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                    <p class="font-medium text-lg">
                      ГРСлар сони
                    </p>
                    <p class="ml-auto">{{ formatNumber(activeDistrict.data.gas.count_hydro_power) }}</p>
                  </div>
                  <div class="flex items-center gap-2 mt-5 pb-5 border-b">
                    <p class="font-medium text-lg">
                      ГТПлар сони
                    </p>
                    <p class="ml-auto">{{ formatNumber(activeDistrict.data.gas.count_gtp) }}</p>
                  </div>
                  <div class="hidden max_big:block mt-5">
                    <info
                        name="ГРП демонтаж"
                        :class-color="getColorClass(activeDistrict.district_id, 'grp_dismantling')"
                        :fill="getColorByKey(activeDistrict.district_id, 'grp_dismantling')"
                        :actual="activeDistrict.data.gas.grp_dismantling_actual"
                        :monthly="activeDistrict.data.gas.grp_dismantling_monthly"
                    />
                    <info
                        name="Газ кувурларини мукаммал тамирлаш"
                        :class-color="getColorClass(activeDistrict.district_id, 'gas_pipe_repair')"
                        :fill="getColorByKey(activeDistrict.district_id, 'gas_pipe_repair')"
                        :actual="activeDistrict.data.gas.gas_pipe_repair_actual"
                        :monthly="activeDistrict.data.gas.gas_pipe_repair_monthly"
                    />
                    <info
                        name="Иссиклик козонхоналарни модернизация килиш ва мукаммал тамирлаш"
                        :class-color="getColorClass(activeDistrict.district_id, 'modernization_thermal_boiler_houses_monthly')"
                        :fill="getColorByKey(activeDistrict.district_id, 'modernization_thermal_boiler_houses_monthly')"
                        :actual="activeDistrict.data.gas.modernization_thermal_boiler_houses_actual"
                        :monthly="activeDistrict.data.gas.modernization_thermal_boiler_houses_monthly"
                    />
                    <info
                        name="Вилоятдаги 223 та саноат корхоналарда ташкилий техник тадбирларни бажариш"
                        :class-color="getColorClass(activeDistrict.district_id, 'plan_for_carrying_organizational_monthly')"
                        :fill="getColorByKey(activeDistrict.district_id, 'plan_for_carrying_organizational_monthly')"
                        :actual="activeDistrict.data.gas.plan_for_carrying_organizational_actual"
                        :monthly="activeDistrict.data.gas.plan_for_carrying_organizational_monthly"
                    />
                    <info
                        name="Газ кувурларини босим остида синаш"
                        :class-color="getColorClass(activeDistrict.district_id, 'pressure_testing_gas_pipelines_actual')"
                        :fill="getColorByKey(activeDistrict.district_id, 'pressure_testing_gas_pipelines_actual')"
                        :actual="activeDistrict.data.gas.pressure_testing_gas_pipelines_actual"
                        :monthly="activeDistrict.data.gas.pressure_testing_gas_pipelines_monthly"
                    />
                    <info
                        name="АГТКШ ларда юкори кувватли компрессорларниПаст кувватлисига алмаштириш"
                        :class-color="getColorClass(activeDistrict.district_id, 'replacement_high_power_compressors_monthly')"
                        :fill="getColorByKey(activeDistrict.district_id, 'replacement_high_power_compressors_monthly')"
                        :actual="activeDistrict.data.gas.replacement_high_power_compressors_actual"
                        :monthly="activeDistrict.data.gas.replacement_high_power_compressors_monthly"
                    />
                    <info
                        name="Ахоли хонадонларидаги ностандарт горелкаларни алмаштириш"
                        :class-color="getColorClass(activeDistrict.district_id, 'replacement_nonstandard_actual')"
                        :fill="getColorByKey(activeDistrict.district_id, 'replacement_nonstandard_actual')"
                        :actual="activeDistrict.data.gas.replacement_nonstandard_actual"
                        :monthly="activeDistrict.data.gas.replacement_nonstandard_monthly"
                    />
                  </div>
                </div>
              </div>
            </div>
          </Transition>
          <!--          end menu-->
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