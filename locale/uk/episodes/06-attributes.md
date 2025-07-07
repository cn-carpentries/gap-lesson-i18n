---
title: Атрибути та Методи
teaching: 40
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- Оголошення атрибуту
- Встановлення методу
- Вибір зрозумілих способів
- Використання інструментів налагодження

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- Як записувати інформацію в об'єктах GAP

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## Яка функція швидка?

Спробуйте повторно обчислити `AvgOrdOfGroup(M11)` і `AvgOrdOfCollection(M11)`
та порівняти runtime. Зробіть це для нової копії `M11` та для тої, для якої
цей параметр вже був збережений. Що ви бачите?

::::::::::::::::::::::::::::::::::::::::::::::::::

Of course, for any given group the average order of its elements needs to
be calculated only once, as the next time it will return the same value.
However, as we see from the runtimes below, each new call of `AvgOrdOfGroup`
will repeat the same computation again, with slightly varying runtime:

```gap
А:=Альтернативна Група(10);
```

```output
Alt( [ 1 .. 10 ] )
```

```gap
AvgOrdOfCollection(A); час; AvgOrdOfCollection(A); час;
```

```output
2587393/259200
8226
2587393/259200
8118
```

In the last example, the group in question was the same -- we haven't
constructed another copy of `AlternatingGroup(10)`; however, the result
of the calculation was not stored in `A`.

If you need to reuse this value, one option could be to store it in some
variable, but then you should be careful about matching such variables
with corresponding groups, and the code could become quite convoluted
and unreadable. On the other hand, GAP has the notion of an _attribute_ -- a
data structure that is used to accumulate information that an object learns about itself
during its lifetime. Розглянемо наступний приклад:

```gap
G:=Group([ (1,2,3,4,5,6,7,8,9,10,11), (3,7,11,8)(4,10,5,6) ]);
gap> NrConjugacyClasses(G);time;NrConjugacyClasses(G);time;
```

```output
Group([ (1,2,3,4,5,6,7,8,9,10,11), (3,7,11,8)(4,10,5,6) ])
10
39
10
0
```

In this case, the group `G` has 10 conjugacy classes, and it took 39 ms to
establish that in the first call. The second call has zero cost since the
result was stored in `G`, since `NrConjugacyClasses` is an attribute:

```gap
NrConjugacyClass;
```

```output
<Attribute "NrConjugacyClasses">
```

Наша мета тепер - навчитися створювати власні атрибути.

Оскільки у нас вже є функція "AvgOrdOfCollection", яка
робить підрахунок, найпростіший спосіб перетворити її на
атрибут наступним чином:

```gap
AverageOrder := NewAttribute("AverageOrder", IsCollection);
InstallMethod( AverageOrder, "for a collection", [IsCollection], , AvgOrdOfCollection);
```

In this example, first we declared an attribute `AverageOrder` for
objects in the category `IsCollection`, and then installed the function
`AvgOrdOfCollection` as a method for this attribute. Замість виклику
функцію "AvgOrdOfCollection", тепер ми можемо викликати "AverageOrder".

Тепер ми можемо перевірити, що наступні виклики `AverageOrder` з тим же аргументом
виконуються за нульовими витратами. У цьому прикладі час зменшується з більше ніж
16 секунд до нуля:

```gap
S:=SymmetricGroup(10);; AverageOrder(S); час; AverageOrder(S); час;
```

```output
39020911/3628800
16445
39020911/3628800
0
```

Ви можете здивуватися, чому ми оголосили операцію для колекції, і не тільки
для групи, і чому ми встановили неефективний `AvgOrdOfCollection`.
Зрештою, ми вже розробили набагато ефективніші `AvgOrdOfGroup`.

Imagine that you would like to be able to compute an average order
both for a group and for a list which consists of objects having a multiplicative
order. У кожного випадку ви можете мати особливу функцію, як і в нас. If it
could happen that you don't know in advance the type of the object in question,
you may add checks into the code and dispatch to a suitable function. This could
quickly become complicated if you have several different functions for various
types of objects. Замість цього атрибути є пучки функцій, називаються
_методи_, і GAP-\* вибір \* буде обрати найбільш ефективний метод
на основі всіх аргументів.

Щоб проілюструвати це, ми тепер встановимо метод для групи "AverageOrder":

```gap
InstallMethod( AverageOrder, [IsGroup], AvgOrdOfGroup);
```

Якщо ви застосуєте його до групи, чию "AverageOrder" вже обчислено, нічого
не станеться, оскільки GAP використовуватиме збережене значення. Однак, для новоствореної групи,
буде викликано новим методом:

```gap
S:=SymmetricGroup(10);; AverageOrder(S); час; AverageOrder(S); час;
```

```output
39020911/3628800
26
39020911/3628800
0
```

:::::::::::::::::::::::::::::::::::::::::  callout

## Який метод називається

- Спробуйте викликати "AverageOrder" для колекції, яка не є групою
  (список елементів групи та/або клас кон'югації елементів).

- Debugging tools like `TraceMethods` may help you see which method is
  being called.

- `ApplicableMethod` у комбінації з `PageSource` може направити вас на вихідний код
  з усіма коментарями.

::::::::::::::::::::::::::::::::::::::::::::::::::

_властивість_ - корисний для булевів. Він може бути створений використовуючи `NewProperty`

```gap
IsIntegerAverageOrder := NewProperty("IsIntegerAverageOrder", IsCollection);
```

Тепер ми встановимо метод для колекції "IsIntegerAverageOrder".
Observe that it is never necessary to create
a function first and then install it as a method. The following method installation
instead creates a new function as one of its arguments:

```gap
InstallMethod( IsIntegerAverageOrder,
  "for a collection",
  [IsCollection],
  coll -> IsInt( AverageOrder( coll ) )
);
```

Зверніть увагу, що через `AverageOrder` є атрибутом, він піклується про вибір
найбільш підходящий метод.

:::::::::::::::::::::::::::::::::::::::::  callout

## Чи існує такий метод?

Поз. "No-method-found" is a special kind of error, and there are tools to
investigate such errors: see `?ShowArguments`, `?ShowDetails`, `?ShowMethods`
and `?ShowOtherMethods`.

::::::::::::::::::::::::::::::::::::::::::::::::::

The following calculation shows that despite our success with calculating
the average order for large permutation groups via conjugacy classes of
elements, for pc groups from the Small Groups Library it could be faster
to iterate over their elements than to calculate conjugacy classes:

```gap
l:=Список([1..1000],i->Смолл Група(1536,i));Список (l,AvgOrdOfGroup);час;
```

```output
56231
```

```gap
l:=Список([1..1000],i->Смолл Група(1536,i));Список (l,AvgOrdOfCollection);час;
```

```output
9141
```

:::::::::::::::::::::::::::::::::::::::  challenge

## Не панікуйте!

- Install a method for `IsPcGroup` that iterates over the group elements
  instead of calculations its conjugacy classes.

- Оцінка практичних кордонів його здійсненості. Ви можете знайти приклад
  групи pc, де ітерація повільніша за розрахунок класів кон'югації?

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- _Позиційні_ об'єкти можуть накопичувати інформацію про себе протягом свого життя.
- Це означає, що наступного разу збережена інформація може бути отримана за нульову ціну.
- - Методи\* - пучки функцій. GAP \* обирає найбільш ефективний метод на основі типу всіх аргументів.
- 'Без методу' є спеціальним видом помилки з корисними інструментами налагодження допомагає його розуміти.

::::::::::::::::::::::::::::::::::::::::::::::::::


