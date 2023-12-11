[![Check code style](https://github.com/FormalLanguageConstrainedPathQuerying/formal-lang-course/actions/workflows/code_style.yml/badge.svg)](https://github.com/FormalLanguageConstrainedPathQuerying/formal-lang-course/actions/workflows/code_style.yml)
[![Code style](https://img.shields.io/badge/Code%20style-black-000000.svg)](https://github.com/psf/black)
---
# Formal Language Course

Курс по формальным языкам: шаблон структуры репозитория для выполнения домашних работ,
а также материалы курса и другая сопутствующая информация.

Актуальное:
- [Таблица с текущими результатами](https://docs.google.com/spreadsheets/d/1-vx82auNr0PQDQ3SwA7IYewZyOC9iHIaoX1w1qRUZ3I/edit?usp=sharing)
- [Список задач](https://github.com/FormalLanguageConstrainedPathQuerying/formal-lang-course/tree/main/tasks)
- [Стиль кода как референс](https://www.python.org/dev/peps/pep-0008/)
- [Материалы по курсу](https://github.com/FormalLanguageConstrainedPathQuerying/formal-lang-course/blob/main/docs/lecture_notes/Formal_language_course.pdf)
- [О достижимости с ограничениями в терминах формальных языков](https://github.com/FormalLanguageConstrainedPathQuerying/FormalLanguageConstrainedReachability-LectureNotes)
- Классика по алгоритмам синтаксического анализа: [Dick Grune, Ceriel J. H. Jacobs, "Parsing Techniques A Practical Guide"](https://link.springer.com/book/10.1007/978-0-387-68954-8#bibliographic-information)
- Классика по теории формальных языков: [M. A. Harrison. 1978. "Introduction to Formal Language Theory"](https://dl.acm.org/doi/book/10.5555/578595)
- Свежее по теории автоматов и их применению в различных областях: [Editors: Jean-Éric Pin. 2021. "Handbook of Automata Theory"](https://ems.press/books/standalone/172)

Технологии:
- Python 3.8+
- Pytest для unit тестирования
- GitHub Actions для CI
- Google Colab для постановки и оформления экспериментов
- Сторонние пакеты из `requirements.txt` файла
- Английский язык для документации или самодокументирующийся код

## Работа с проектом

- Для выполнения домашних практических работ необходимо сделать `fork` этого репозитория к себе в `GitHub`.
- Рекомендуется установить [`pre-commit`](https://pre-commit.com/#install) для поддержания проекта в адекватном состоянии.
  - Установить `pre-commit` можно выполнив следующую команду в корне вашего проекта:
    ```shell
    pre-commit install
    ```
  - Отформатировать код в соответствии с принятым стилем можно выполнив следующую команду в корне вашего проекта:
    ```shell
    pre-commit run --all-files
    ```
- Ссылка на свой `fork` репозитория размещается в [таблице](https://docs.google.com/spreadsheets/d/1-vx82auNr0PQDQ3SwA7IYewZyOC9iHIaoX1w1qRUZ3I/edit?usp=sharing) курса с результатами.
- В свой репозиторий необходимо добавить проверяющих с `admin` правами на чтение, редактирование и проверку `pull-request`'ов.

## Домашние практические работы

### Дедлайны

- **мягкий**: TODO 23:59
- **жёсткий**: TODO 23:59

### Выполнение домашнего задания

- Каждое домашнее задание выполняется в отдельной ветке. Ветка должна иметь осмысленное консистентное название.
- При выполнении домашнего задания в новой ветке необходимо открыть соответствующий `pull-request` в `main` вашего `fork`.
- `Pull-request` снабдить понятным названием и описанием с соответствующими пунктами прогресса.
- Проверка заданий осуществляется посредством `review` вашего `pull-request`.
- Как только вы считаете, что задание выполнено, вы можете запросить `review` у проверяющего.
  - Если `review` запрошено **до мягкого дедлайна**, то вам гарантированна дополнительная проверка (до жёсткого дедлайна), позволяющая исправить замечания до наступления жёсткого дедлайна.
  - Если `review` запрошено **после мягкого дедлайна**, но **до жесткого дедлайна**, задание будет проверено, но нет гарантий, что вы успеете его исправить.
- Когда проверка будет пройдена, и задание **зачтено**, его необходимо `merge` в `main` вашего `fork`.
- Результаты выполненных заданий будут повторно использоваться в последующих домашних работах.

### Опциональные домашние задания
Часть задач, связанных с работой с GPGPU, будет помечена как опциональная. Это означает что и без их выполнения (при идеальном выполнении остальных задач) можно набрать полный балл за курс.

### Получение оценки за домашнюю работу

- Если ваша работа **зачтена** _до_ **жёсткого дедлайна**, то вы получаете **полный балл за домашнюю работу**.
- Если ваша работа **зачтена** _после_ **жёсткого дедлайна**, то вы получаете **половину полного балла за домашнюю работу**.
  - Если ревью было запрошено _до_ **жёсткого дедлайна** и задача зачтена сразу без замечаний, то вы всё ещё получаете **полный балл за домашнюю работу**.

## Код

- Исходный код практических задач по программированию размещайте в папке `project`.
- Файлам и модулям даем осмысленные имена, в соответствии с официально принятым стилем.
- Структурируем код, используем как классы, так и отдельно оформленные функции. Чем понятнее код, тем быстрее его проверять и тем больше у вас будет шансов получить полный балл.

## Тесты

- Тесты для домашних заданий размещайте в папке `tests`.
- Формат именования файлов с тестами `test_[какой модуль\класс\функцию тестирует].py`.
- Для работы с тестами рекомендуется использовать [`pytest`](https://docs.pytest.org/en/6.2.x/).
- Для запуска тестов необходимо из корня проекта выполнить следующую команду:
  ```shell
  python ./scripts/run_tests.py
  ```

## Эксперименты

- Для выполнения экспериментов потребуется не только код, но окружение и некоторая его настройка.
- Эксперименты должны быть воспроизводимыми (например, проверяющими).
- Эксперимент (настройка, замеры, результаты, анализ результатов) оформляется как Python-ноутбук, который публикуется на GitHub.
  - В качестве окружения для экспериментов с GPGPU (опциональные задачи) можно использовать [`Google Colab`](https://research.google.com/colaboratory/) ноутбуки. Для его создания требуется только учетная запись `Google`.
  - В `Google Colab` ноутбуке выполняется вся настройка, пишется код для экспериментов, подготовки отчетов и графиков.

## Структура репозитория

```text
.
├── .github - файлы для настройки CI и проверок
├── docs - текстовые документы и материалы по курсу
├── project - исходный код домашних работ
├── scripts - вспомогательные скрипты для автоматизации разработки
├── tasks - файлы с описанием домашних заданий
├── tests - директория для unit-тестов домашних работ
├── README.md - основная информация о проекте
└── requirements.txt - зависимости для настройки репозитория
```

## Контакты

- Семен Григорьев [@gsvgit](https://github.com/gsvgit)
- Егор Орачев [@EgorOrachyov](https://github.com/EgorOrachyov)
- Вадим Абзалов [@vdshk](https://github.com/vdshk)
- Рустам Азимов [@rustam-azimov](https://github.com/rustam-azimov)
- Екатерина Шеметова [@katyacyfra](https://github.com/katyacyfra)

## Язык запросов к графам

```
prog = List<stmt>

stmt =
    bind of var * expr
  | print of expr

val =
    String of string
  | Int of int
  | Bool of bool
  | Graph of graph
  | Labels of labels
  | Vertices of vertices
  | Edges of edges

expr =
    Var of var                   // переменные
  | Val of val                   // константы
  | Set_start of Set<val> * expr // задать множество стартовых состояний
  | Set_final of Set<val> * expr // задать множество финальных состояний
  | Add_start of Set<val> * expr // добавить состояния в множество стартовых
  | Add_final of Set<val> * expr // добавить состояния в множество финальных
  | Get_start of expr            // получить множество стартовых состояний
  | Get_final of expr            // получить множество финальных состояний
  | Get_reachable of expr        // получить все пары достижимых вершин
  | Get_vertices of expr         // получить все вершины
  | Get_edges of expr            // получить все рёбра
  | Get_labels of expr           // получить все метки
  | Map of lambda * expr         // классический map
  | Filter of lambda * expr      // классический filter
  | Load of expr                 // загрузка графа
  | Intersect of expr * expr     // пересечение языков
  | Concat of expr * expr        // конкатенация языков
  | Union of expr * expr         // объединение языков
  | Star of expr                 // замыкание языков (звезда Клини)
  | Smb of expr                  // единичный переход
  | Contains of expr * expr      // Вхождение элемента в множество
  | Set of List<expr>            // Множество элементов

lambda =
    lambda = var * expr
```

## Конкретный синтаксис

```
prog --> (statement ENDOFLINE)*

statement -->
    var ASSIGN expr SEMICOLON
  | 'print' expr SEMICOLON

var --> init_letter var_string
init_letter --> CHAR | '_'
var_string --> (init_letter | DIGIT)*

expr -->
    LEFT_PARENTHESIS expr RIGHT_PARENTHESIS
  | var
  | val
  | map
  | filter
  | intersect
  | concat
  | union
  | star
  | contains

lambda --> LEFT_CURLY_BRACE 'fun' var '->' expr RIGHT_CURLY_BRACE

map --> 'map' LEFT_PARENTHESIS lambda COMMA expr RIGHT_PARENTHESIS

filter --> 'filter' LEFT_PARENTHESIS lambda COMMA expr RIGHT_PARENTHESIS

intersert --> 'intersect' LEFT_PARENTHESIS expr COMMA expr RIGHT_PARENTHESIS

concat --> 'concat' LEFT_PARENTHESIS expr COMMA expr RIGHT_PARENTHESIS

union --> 'union' LEFT_PARENTHESIS expr COMMA expr RIGHT_PARENTHESIS

star --> LEFT_PARENTHESIS expr RIGHT_PARENTHESIS '*'

contains --> expr 'in' set

val -->
    LEFT_PARENTHESIS val RIGHT_PARENTHESIS
  | QUOTE string QUOTE
  | INT
  | BOOL
  | graph
  | labels
  | vertices
  | edges

string --> (CHAR | INT | '.' | '?' | '*')*

graph -->
    'set_start' LEFT_PARENTHESIS vertices COMMA graph RIGHT_PARENTHESIS
  | 'set_final' LEFT_PARENTHESIS vertices COMMA graph RIGHT_PARENTHESIS
  | 'add_start' LEFT_PARENTHESIS vertices COMMA graph RIGHT_PARENTHESIS
  | 'add_final' LEFT_PARENTHESIS vertices COMMA graph RIGHT_PARENTHESIS
  | 'get_graph' LEFT_PARENTHESIS path RIGHT_PARENTHESIS
  | var

path --> QUOTE string QUOTE | var

vertices -->
    'get_start' LEFT_PARENTHESIS graph RIGHT_PARENTHESIS
  | 'get_final' LEFT_PARENTHESIS graph RIGHT_PARENTHESIS
  | 'get_reachable' LEFT_PARENTHESIS graph RIGHT_PARENTHESIS
  | 'get_vertices' LEFT_PARENTHESIS graph RIGHT_PARENTHESIS
  | set
  | var

labels --> 'get_labels' LEFT_PARENTHESIS graph RIGHT_PARENTHESIS | set

edges --> 'get_edges' LEFT_PARENTHESIS graph RIGHT_PARENTHESIS | set

set --> LEFT_CURLY_BRACE expr (COMMA expr)* RIGHT_CURLY_BRACE
  | 'set()'
  | LEFT_CURLY_BRACE ( LEFT_PARENTHESIS INT COMMA (val | var) COMMA INT RIGHT_PARENTHESIS )* RIGHT_CURLY_BRACE

ASSIGN ---> '='
BOOL --> 'true' | 'false'
CHAR --> [a-z] | [A-Z]
COMMA --> ','
DIGIT --> [0-9]
ENDOFLINE --> [\n]
INT --> '0' | '-'? [1-9][0-9]*
LEFT_CURLY_BRACE --> '{'
LEFT_PARENTHESIS --> '('
QUOTE --> '"'
RIGHT_CURLY_BRACE --> '}'
RIGHT_PARENTHESIS --> ')'
SEMICOLON --> ';'
```

## Примеры

### Загрузка графа и простейшая работа с ним
```
graph = get_graph("some/path"); // Загрузка графа по пути
vertices = get_vertices(graph); // Взятие вершин загруженного графа
graph_upd = set_start(vertices, graph); // Назначение всех вершин стартовыми
print vertices; // Печать меток
```

### Работа с регулярными запросами
```
a = union ("A", "a"); // Объединение двух регулярных запросов
b = (union ("B", b))*; // Объединение двух регулярных запросов
print concat (a, b); // Конкатенация регулярных запросов и их печать
```

### Работа с вершинами графа
```
graph = get_graph("some/path"); // Загрузка графа по пути
graph = set_start(get_vertices(graph), graph); // Установка всех вершин графа стартовыми
graph = add_final(set(2, 3), graph); // Установка множества вершин финальными
print get_final(graph); // Печать результата
```

### Работа с функциями
```
graph = get_graph("some/path"); // Загрузка графа по пути
new_graph = get_graph("another/path"); // Загрузка графа по пути
v = get_vertices(graph); // Получение вершин графа
result = map({fun vert -> add_start(vert, new_graph)}, v); // Добавление вершин первого графа как стартовых в новом графе
filtered = filter({fun x -> x in {1, 2, 3}}, result); // Фильтрация вершин
print result; // Печать результата
```

### Пересечение графа с регулярным запросом
```
graph = get_graph("some/path"); // Загрузка графа по пути
query = "a*b"; // Создание регулярного запроса
result = intersect(graph, query); // Выполнение пересечения
print result; // Печать результата
```
