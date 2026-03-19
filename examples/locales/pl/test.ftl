test-message = { $tasks_count ->
    [0]     Witaj, { $user_name }! Nie masz żadnych zadań.
    [one]   Witaj, { $user_name }! Masz { $tasks_count } zadanie.
    *[other] Witaj, { $user_name }! Masz { $tasks_count } zadań.
}
// test-message-1 = Wiadomość testowa 1
test-message-2 = Wiadomość testowa 2