from washing_machine import WashingMachine, cloth_type


wm = WashingMachine("Samsung", "White")


#сам цикл прання
def laundry_cycle(mode) -> None:
    print(f"\nПочинаю прання в режимі “{cloth_type[mode]["name"]}“")
    print(f"Температура прання: {cloth_type[mode]["temperature"]}")
    print(f"Сила віджиму: {cloth_type[mode]["spin_power"]}")

    wm.mode("прання", 4)
    wm.mode("полоскання", 2)
    wm.mode("віджиму", 1)
    wm.finish("Прання")
    
    return None


# головна функція
def main() -> None:
    #виводить усі види тканини
    for i, el in enumerate(cloth_type):
        print(f"{i + 1}. {el["name"]}: {el["temperature"]}; {el["spin_power"]}")
    
    possible_modes = [str(i + 1) for i, _ in enumerate(cloth_type)]
    mode = input("\nВиберіть режим прання(введіть число): ")

    if not mode in possible_modes:
        print(f"\nРежиму прання “{mode}“ не існує")
        return None
    
    mode = int(mode) - 1

    laundry_cycle(mode)
    
    do_drying = input("Ви хочете щоб пральна машинка зробила сушіння речей(y/n)?")

    if do_drying.lower() == 'y':
        wm.mode("Сушіння", 3)
        wm.finish("Сушіння")

    return None


if __name__ == '__main__':
    main()
