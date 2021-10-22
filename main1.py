import pandas as pd
import matplotlib.pyplot as plt
import os


class DrawingPlots:

    def draw_plots(self, link, size=50, side_x=20, side_y=20):
        # Проверка на наличие директории "Графики", создание данной директории если отсуствует.
        file_path = "Графики"
        if not os.path.exists(file_path):
            try:
                os.mkdir(file_path)
            except OSError:
                print("Создать директорию %s не удалось" % file_path)
            else:
                print("Успешно создана директория %s " % file_path)

        # считываение Json и сздание обьекта dataframe
        iris_data = pd.read_json(link)
        # При большом количестве строк >99 происхлдит разюитиет на несколько графиков
        # выщитывание количесва польность заполненых графиков и проверка что такие имеются
        # Запись адресов проихходит в список
        ln = len(iris_data)
        count_ln = ln//size
        remainder_count = ln % size
        if count_ln > 0:
            start = 0
            return_link = []
            # Итерационная создание графиков в "Графики" по 100 стрчоек таблицы
            for namber_plots in range(count_ln):
                iris_data[start:start+size].plot(x="name", kind="bar", figsize=(side_x, side_y), stacked=False,
                                                 title=f'plots_{namber_plots}')
                plt.savefig('Графики/'+f'plots_{namber_plots}.png')
                plt.close()
                return_link.append('Графики/'+f'plots_{namber_plots}.png')
                start += size
            if remainder_count:
                iris_data[start:start + remainder_count].plot(x="name", kind="bar", figsize=(side_x, side_y),
                                                              stacked=False, title=f'plots_last'
                                                              )
                plt.savefig('Графики/plots_last.png')
                plt.close()
                return_link.append('Графики/plots_last.png')
        else:
            return_link = []
            iris_data[0:remainder_count].plot(x="name", kind="bar", figsize=(side_x, side_y), stacked=False)
            plt.savefig('Графики/' + f'plots_last.png')
            plt.close()
            return_link.append('Графики/plots.png')
        return return_link

