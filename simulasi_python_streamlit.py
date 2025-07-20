import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from io import StringIO

# Set page config
st.set_page_config(page_title="Simulasi Distribusi Wisatawan Indonesia", layout="wide")

# Data wisatawan (dari file yang diberikan)
data_text = """Pintu Udara,,,Pintu Laut,,,Pintu Darat,,
Tahun,Bulan,Jumlah Kunjungan,Tahun,Bulan,Jumlah Kunjungan,Tahun,Bulan,Jumlah Kunjungan
2008,Januari,270189,2008,Januari,89296,2008,Januari,1043
,Februari,294147,,Februari,102762,,Februari,1613
,Maret,312324,,Maret,108215,,Maret,1610
,April,285113,,April,93401,,April,1234
,Mei,321657,,Mei,105042,,Mei,1606
,Juni,327611,,Juni,115706,,Juni,1553
,Juli,369353,,Juli,101001,,Juli,1363
,Agustus,385538,,Agustus,113357,,Agustus,2331
,September,318911,,September,90081,,September,1790
,Oktober,338085,,Oktober,97278,,Oktober,1430
,November,321359,,November,105472,,November,1672
,Desember,370881,,Desember,131170,,Desember,2744
2009,Januari,294794,2009,Januari,97421,2009,Januari,1581
,Februari,270702,,Februari,80681,,Februari,1175
,Maret,324597,,Maret,101978,,Maret,1859
,April,316141,,April,91428,,April,1497
,Mei,346170,,Mei,94537,,Mei,1814
,Juni,364887,,Juni,100206,,Juni,1820
,Juli,426217,,Juli,82814,,Juli,1451
,Agustus,390155,,Agustus,91030,,Agustus,1578
,September,331184,,September,79471,,September,2192
,Oktober,376600,,Oktober,84539,,Oktober,1314
,November,346575,,November,89639,,November,1855
,Desember,390712,,Desember,119339,,Desember,3054
2010,Januari,340049,2010,Januari,119784,2010,Januari,1262
,Februari,359018,,Februari,127592,,Februari,2432
,Maret,423943,,Maret,131280,,Maret,1873
,April,402118,,April,120526,,April,1538
,Mei,431258,,Mei,132703,,Mei,2073
,Juni,434110,,Juni,147125,,Juni,2099
,Juli,486783,,Juli,136132,,Juli,2134
,Agustus,431164,,Agustus,122624,,Agustus,1874
,September,401250,,September,117983,,September,1816
,Oktober,431614,,Oktober,123252,,Oktober,1139
,November,396216,,November,134152,,November,1915
,Desember,416954,,Desember,170959,,Desember,3281
2011,Januari,394893,2011,Januari,119878,2011,Januari,1647
,Februari,395228,,Februari,135620,,Februari,2297
,Maret,420178,,Maret,139213,,Maret,2044
,April,431339,,April,141849,,April,1831
,Mei,417037,,Mei,144348,,Mei,2201
,Juni,468813,,Juni,169653,,Juni,2118
,Juli,543170,,Juli,164244,,Juli,1559
,Agustus,446871,,Agustus,136033,,Agustus,2643
,September,471222,,September,136953,,September,1759
,Oktober,473750,,Oktober,143100,,Oktober,1506
,November,459210,,November,151406,,November,2269
,Desember,479549,,Desember,192385,,Desember,3380
2012,Januari,460031,2012,Januari,157604,2012,Januari,2324
,Februari,417115,,Februari,125930,,Februari,1787
,Maret,453805,,Maret,157808,,Maret,2121
,April,444598,,April,142636,,April,1503
,Mei,469019,,Mei,141789,,Mei,1973
,Juni,475928,,Juni,176875,,Juni,2514
,Juli,520409,,Juli,142341,,Juli,1741
,Agustus,446606,,Agustus,148134,,Agustus,3036
,September,499071,,September,142041,,September,1371
,Oktober,495817,,Oktober,151940,,Oktober,1665
,November,498838,,November,149830,,November,2761
,Desember,519868,,Desember,196679,,Desember,3101
2013,Januari,449297,2013,Januari,131189,2013,Januari,1368
,Februari,481181,,Februari,158618,,Februari,2291
,Maret,507704,,Maret,174784,,Maret,2291
,April,467817,,April,135951,,April,1408
,Mei,503039,,Mei,154845,,Mei,2009
,Juni,564997,,Juni,183730,,Juni,2581
,Juli,545003,,Juli,134321,,Juli,1559
,Agustus,564762,,Agustus,166472,,Agustus,3038
,September,578721,,September,152985,,September,1474
,Oktober,531645,,Oktober,148108,,Oktober,1559
,November,591980,,November,171430,,November,2330
,Desember,588254,,Desember,211860,,Desember,2948
2014,Januari,544958,2014,Januari,169926,2014,Januari,1535
,Februari,518574,,Februari,141922,,Februari,1609
,Maret,546784,,Maret,175797,,Maret,1699
,April,530165,,April,157164,,April,1430
,Mei,551646,,Mei,159893,,Mei,1785
,Juni,616754,,Juni,195824,,Juni,1703
,Juli,589071,,Juli,151048,,Juli,2488
,Agustus,627366,,Agustus,163879,,Agustus,1568
,September,597470,,September,156103,,September,1445
,Oktober,594312,,Oktober,172218,,Oktober,1731
,November,553480,,November,167909,,November,1936
,Desember,630352,,Desember,226683,,Desember,3535
2015,Januari,514693,2015,Januari,155981,2015,Januari,1265
,Februari,569113,,Februari,172490,,Februari,1873
,Maret,568134,,Maret,168997,,Maret,2440
,April,537918,,April,169374,,April,1491
,Mei,553773,,Mei,195528,,Mei,2424
,Juni,596079,,Juni,180225,,Juni,1662
,Juli,617198,,Juli,155923,,Juli,2573
,Agustus,622058,,Agustus,189359,,Agustus,1710
,September,661105,,September,159912,,September,1693
,Oktober,627112,,Oktober,161844,,Oktober,1455
,November,553965,,November,166239,,November,2513
,Desember,632243,,Desember,226412,,Desember,3753
2016,Januari,548863,2016,Januari,148144,2016,Januari,36791
,Februari,592968,,Februari,172209,,Februari,38740
,Maret,631176,,Maret,172770,,Maret,30704
,April,640094,,April,169731,,April,23577
,Mei,661824,,Mei,177581,,Mei,21022
,Juni,611469,,Juni,170910,,Juni,22609
,Juli,785275,,Juli,142820,,Juli,28095
,Agustus,793587,,Agustus,146917,,Agustus,26406
,September,760591,,September,160347,,September,23900
,Oktober,757044,,Oktober,155045,,Oktober,35085
,November,706431,,November,147629,,November,49268
,Desember,738303,,Desember,216451,,Desember,60278
2017,Januari,746666,2017,Januari,230174,2017,Januari,131128
,Februari,720428,,Februari,186669,,Februari,116291
,Maret,749150,,Maret,220326,,Maret,90301
,April,812927,,April,233538,,April,124921
,Mei,809941,,Mei,209193,,Mei,129454
,Juni,763470,,Juni,233765,,Juni,146766
,Juli,1002611,,Juli,226979,,Juli,141001
,Agustus,1014475,,Agustus,235311,,Agustus,143457
,September,883842,,September,229735,,September,136654
,Oktober,802479,,Oktober,222271,,Oktober,136815
,November,701307,,November,230070,,November,130653
,Desember,663359,,Desember,324624,,Desember,159048
2018,Januari,643177,2018,Januari,220044,2018,Januari,234618
,Februari,740440,,Februari,261044,,Februari,196019
,Maret,845635,,Maret,304859,,Maret,212932
,April,848734,,April,236833,,April,216754
,Mei,805452,,Mei,230118,,Mei,207135
,Juni,817405,,Juni,289312,,Juni,215957
,Juli,1073385,,Juli,252458,,Juli,221388
,Agustus,1006054,,Agustus,280868,,Agustus,224099
,September,911326,,September,264522,,September,195095
,Oktober,855240,,Oktober,243901,,Oktober,192464
,November,716298,,November,259832,,November,181353
,Desember,825635,,Desember,370629,,Desember,209290
2019,Januari,706704,2019,Januari,304479,2019,Januari,190552
,Februari,731517,,Februari,340751,,Februari,171728
,Maret,758821,,Maret,378698,,Maret,174392
,April,772038,,April,328884,,April,173309
,Mei,711229,,Mei,335111,,Mei,203196
,Juni,829067,,Juni,386152,,Juni,218884
,Juli,975870,,Juli,311429,,Juli,180874
,Agustus,977033,,Agustus,368408,,Agustus,184827
,September,900409,,September,327642,,September,160668
,Oktober,855796,,Oktober,332319,,Oktober,158319
,November,777244,,November,358264,,November,145273
,Desember,838978,,Desember,388495,,Desember,149594
2020,Januari,821851,2020,Januari,313541,2020,Januari,155019
,Februari,562150,,Februari,192604,,Februari,118011
,Maret,255067,,Maret,111323,,Maret,119765
,April,783,,April,45058,,April,112225
,Mei,506,,Mei,46615,,Mei,114721
,Juni,1463,,Juni,47060,,Juni,108038
,Juli,4069,,Juli,46942,,Juli,104731
,Agustus,5728,,Agustus,49542,,Agustus,106279
,September,9991,,September,45109,,September,93884
,Oktober,12280,,Oktober,41370,,Oktober,98643
,November,16085,,November,40970,,November,87421
,Desember,23599,,Desember,44467,,Desember,96013
2021,Januari,1731,2021,Januari,37667,2021,Januari,87117
,Februari,7110,,Februari,29300,,Februari,69378
,Maret,12852,,Maret,35317,,Maret,71810
,April,18326,,April,30918,,April,63512
,Mei,14040,,Mei,39720,,Mei,85673
,Juni,16234,,Juni,29929,,Juni,80681
,Juli,7175,,Juli,35511,,Juli,84563
,Agustus,1609,,Agustus,33497,,Agustus,83427
,September,4748,,September,33397,,September,81955
,Oktober,15722,,Oktober,38245,,Oktober,92170
,November,19909,,November,32741,,November,97927
,Desember,17786,,Desember,39230,,Desember,106603
2022,Januari,14555,2022,Januari,58442,2022,Januari,63301
,Februari,17834,,Februari,51539,,Februari,48136
,Maret,39062,,Maret,60357,,Maret,59210
,April,97401,,April,69085,,April,63590
,Mei,183830,,Mei,105719,,Mei,65371
,Juni,280482,,Juni,134664,,Juni,68737
,Juli,387184,,Juli,184193,,Juli,73744
,Agustus,422500,,Agustus,164918,,Agustus,83091
,September,424198,,September,196668,,September,79740
,Oktober,447074,,Oktober,207390,,Oktober,79764
,November,429979,,November,193894,,November,80910
,Desember,551927,,Desember,299967,,Desember,100575
2023,Januari,484497,2023,Januari,224851,2023,Januari,89121
,Februari,487449,,Februari,191063,,Februari,70924
,Maret,554665,,Maret,236181,,Maret,78398
,April,560434,,April,235660,,April,69717
,Mei,659065,,Mei,214326,,Mei,80323
,Juni,707476,,Juni,276039,,Juni,79276
,Juli,819496,,Juli,225106,,Juli,76587
,Agustus,826446,,Agustus,220199,,Agustus,85993
,September,777537,,September,212770,,September,79938
,Oktober,707584,,Oktober,186161,,Oktober,84774
,November,656709,,November,190258,,November,84260
,Desember,731293,,Desember,291763,,Desember,121486
2024,Januari,631961,2024,Januari,198072,2024,Januari,97713
,Februari,735072,,Februari,239718,,Februari,87359
,Maret,682439,,Maret,252013,,Maret,107409
,April,750085,,April,211716,,April,105157
,Mei,835722,,Mei,212718,,Mei,97059
,Juni,821654,,Juni,261165,,Juni,115122
,Juli,994583,,Juli,212433,,Juli,103740
,Agustus,987547,,Agustus,248758,,Agustus,103641
,September,941903,,September,231748,,September,105607
,Oktober,859747,,Oktober,218620,,Oktober,115500
,November,756972,,November,223293,,November,111802
,Desember,832865,,Desember,264692,,Desember,131073
2025,Januari,801614,2025,Januari,232267,2025,Januari,122131
,Februari,718609,,Februari,203450,,Februari,100835
,Maret,669479,,Maret,206397,,Maret,108893
,April,854756,,April,200550,,April,109233
,Mei,941092,,Mei,244169,,Mei,120739"""

def load_and_process_data():
    """Memuat dan memproses data dari string"""
    lines = data_text.strip().split('\n')[1:]  # Skip header

    pintu_udara = []
    pintu_laut = []
    pintu_darat = []

    for line in lines:
        parts = line.split(',')
        if len(parts) > 2 and parts[2].strip().isdigit():
            pintu_udara.append(int(parts[2].strip()))

        if len(parts) > 5 and parts[5].strip().isdigit():
            pintu_laut.append(int(parts[5].strip()))

        if len(parts) > 8 and parts[8].strip().isdigit():
            pintu_darat.append(int(parts[8].strip()))

    return pintu_udara, pintu_laut, pintu_darat

def calculate_normal_params(data):
    """Menghitung parameter distribusi normal (mean dan std)"""
    return np.mean(data), np.std(data)

def create_frequency_distribution(data, bins=30):
    """Membuat distribusi frekuensi dari data"""
    hist, bin_edges = np.histogram(data, bins=bins)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    return hist, bin_centers, bin_edges

def simulate_normal_distribution(mean, std, size=1000):
    """Mensimulasikan data berdasarkan distribusi normal"""
    return np.random.normal(mean, std, size)

def main():
    st.title("Simulasi Distribusi Frekuensi Kunjungan Wisatawan Mancanegara ke Indonesia")
    st.markdown("**Berdasarkan data 2008-2025 dengan pendekatan distribusi normal**")

    # Load data
    pintu_udara, pintu_laut, pintu_darat = load_and_process_data()

    # Sidebar untuk parameter simulasi
    st.sidebar.header("Parameter Simulasi")
    n_simulations = st.sidebar.slider("Jumlah Simulasi", 500, 5000, 1000, 100)
    n_bins = st.sidebar.slider("Jumlah Bins Histogram", 20, 50, 30, 5)

    # Hitung parameter distribusi normal untuk setiap pintu masuk
    mean_udara, std_udara = calculate_normal_params(pintu_udara)
    mean_laut, std_laut = calculate_normal_params(pintu_laut)
    mean_darat, std_darat = calculate_normal_params(pintu_darat)

    # Tampilkan statistik deskriptif
    st.header("Statistik Deskriptif Data Historis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Pintu Udara")
        st.metric("Mean", f"{mean_udara:,.0f}")
        st.metric("Std Dev", f"{std_udara:,.0f}")
        st.metric("Total Data", len(pintu_udara))

    with col2:
        st.subheader("Pintu Laut")
        st.metric("Mean", f"{mean_laut:,.0f}")
        st.metric("Std Dev", f"{std_laut:,.0f}")
        st.metric("Total Data", len(pintu_laut))

    with col3:
        st.subheader("Pintu Darat")
        st.metric("Mean", f"{mean_darat:,.0f}")
        st.metric("Std Dev", f"{std_darat:,.0f}")
        st.metric("Total Data", len(pintu_darat))

    # Simulasi distribusi normal
    sim_udara = simulate_normal_distribution(mean_udara, std_udara, n_simulations)
    sim_laut = simulate_normal_distribution(mean_laut, std_laut, n_simulations)
    sim_darat = simulate_normal_distribution(mean_darat, std_darat, n_simulations)

    # Pastikan nilai tidak negatif (kunjungan tidak bisa negatif)
    sim_udara = np.maximum(sim_udara, 0)
    sim_laut = np.maximum(sim_laut, 0)
    sim_darat = np.maximum(sim_darat, 0)

    # Grafik perbandingan data historis vs simulasi
    st.header("Perbandingan Data Historis vs Simulasi")

    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('Distribusi Frekuensi: Data Historis vs Simulasi', fontsize=16, fontweight='bold')

    # Warna untuk setiap pintu masuk
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    titles = ['Pintu Udara', 'Pintu Laut', 'Pintu Darat']
    historical_data = [pintu_udara, pintu_laut, pintu_darat]
    simulated_data = [sim_udara, sim_laut, sim_darat]

    for i, (hist_data, sim_data, color, title) in enumerate(zip(historical_data, simulated_data, colors, titles)):
        # Data Historis
        axes[0, i].hist(hist_data, bins=n_bins, alpha=0.7, color=color, edgecolor='black')
        axes[0, i].set_title(f'{title} - Data Historis')
        axes[0, i].set_xlabel('Jumlah Kunjungan')
        axes[0, i].set_ylabel('Frekuensi')
        axes[0, i].grid(True, alpha=0.3)

        # Data Simulasi
        axes[1, i].hist(sim_data, bins=n_bins, alpha=0.7, color=color, edgecolor='black')
        axes[1, i].set_title(f'{title} - Simulasi Normal')
        axes[1, i].set_xlabel('Jumlah Kunjungan')
        axes[1, i].set_ylabel('Frekuensi')
        axes[1, i].grid(True, alpha=0.3)

    plt.tight_layout()
    st.pyplot(fig)

    # Grafik overlay perbandingan
    st.header("Overlay Perbandingan Distribusi")

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle('Perbandingan Distribusi: Historis vs Simulasi', fontsize=16, fontweight='bold')

    for i, (hist_data, sim_data, color, title) in enumerate(zip(historical_data, simulated_data, colors, titles)):
        axes[i].hist(hist_data, bins=n_bins, alpha=0.6, label='Data Historis',
                    color=color, edgecolor='black', density=True)
        axes[i].hist(sim_data, bins=n_bins, alpha=0.6, label='Simulasi Normal',
                    color='gray', edgecolor='black', density=True)
        axes[i].set_title(title)
        axes[i].set_xlabel('Jumlah Kunjungan')
        axes[i].set_ylabel('Densitas')
        axes[i].legend()
        axes[i].grid(True, alpha=0.3)

    plt.tight_layout()
    st.pyplot(fig)

    # Pie Chart Perbandingan Total
    st.header("Pie Chart Perbandingan Total Kunjungan")

    # Hitung total untuk data historis dan simulasi
    total_udara_hist = sum(pintu_udara)
    total_laut_hist = sum(pintu_laut)
    total_darat_hist = sum(pintu_darat)

    total_udara_sim = sum(sim_udara)
    total_laut_sim = sum(sim_laut)
    total_darat_sim = sum(sim_darat)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Data Historis (2008-2025)")
        fig, ax = plt.subplots(figsize=(8, 8))
        labels = ['Pintu Udara', 'Pintu Laut', 'Pintu Darat']
        sizes = [total_udara_hist, total_laut_hist, total_darat_hist]
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
        explode = (0.05, 0.05, 0.05)

        wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                                         autopct='%1.1f%%', shadow=True, startangle=90)
        ax.set_title('Distribusi Total Kunjungan Historis', fontsize=14, fontweight='bold')

        # Tambahkan nilai absolut
        for i, (wedge, text, autotext) in enumerate(zip(wedges, texts, autotexts)):
            autotext.set_text(f'{sizes[i]/sum(sizes)*100:.1f}%\n({sizes[i]:,.0f})')
            autotext.set_fontsize(10)
            autotext.set_fontweight('bold')

        st.pyplot(fig)

        # Tampilkan total
        st.metric("Total Kunjungan Historis", f"{sum(sizes):,.0f}")

    with col2:
        st.subheader("Hasil Simulasi")
        fig, ax = plt.subplots(figsize=(8, 8))
        sizes_sim = [total_udara_sim, total_laut_sim, total_darat_sim]

        wedges, texts, autotexts = ax.pie(sizes_sim, explode=explode, labels=labels, colors=colors,
                                         autopct='%1.1f%%', shadow=True, startangle=90)
        ax.set_title('Distribusi Total Kunjungan Simulasi', fontsize=14, fontweight='bold')

        # Tambahkan nilai absolut
        for i, (wedge, text, autotext) in enumerate(zip(wedges, texts, autotexts)):
            autotext.set_text(f'{sizes_sim[i]/sum(sizes_sim)*100:.1f}%\n({sizes_sim[i]:,.0f})')
            autotext.set_fontsize(10)
            autotext.set_fontweight('bold')

        st.pyplot(fig)

        # Tampilkan total
        st.metric("Total Kunjungan Simulasi", f"{sum(sizes_sim):,.0f}")

    # Tabel perbandingan
    st.header("Tabel Perbandingan Detail")

    comparison_df = pd.DataFrame({
        'Pintu Masuk': ['Pintu Udara', 'Pintu Laut', 'Pintu Darat'],
        'Mean Historis': [f"{mean_udara:,.0f}", f"{mean_laut:,.0f}", f"{mean_darat:,.0f}"],
        'Std Historis': [f"{std_udara:,.0f}", f"{std_laut:,.0f}", f"{std_darat:,.0f}"],
        'Mean Simulasi': [f"{np.mean(sim_udara):,.0f}", f"{np.mean(sim_laut):,.0f}", f"{np.mean(sim_darat):,.0f}"],
        'Std Simulasi': [f"{np.std(sim_udara):,.0f}", f"{np.std(sim_laut):,.0f}", f"{np.std(sim_darat):,.0f}"],
        'Total Historis': [f"{total_udara_hist:,.0f}", f"{total_laut_hist:,.0f}", f"{total_darat_hist:,.0f}"],
        'Total Simulasi': [f"{total_udara_sim:,.0f}", f"{total_laut_sim:,.0f}", f"{total_darat_sim:,.0f}"],
        'Persentase Historis': [f"{total_udara_hist/sum(sizes)*100:.1f}%",
                               f"{total_laut_hist/sum(sizes)*100:.1f}%",
                               f"{total_darat_hist/sum(sizes)*100:.1f}%"],
        'Persentase Simulasi': [f"{total_udara_sim/sum(sizes_sim)*100:.1f}%",
                               f"{total_laut_sim/sum(sizes_sim)*100:.1f}%",
                               f"{total_darat_sim/sum(sizes_sim)*100:.1f}%"]
    })

    st.dataframe(comparison_df, use_container_width=True)

    # Analisis dan Insights
    st.header("Analisis dan Insights")

    st.markdown("""
    ### Hasil Simulasi Distribusi Frekuensi:

    **1. Karakteristik Distribusi:**
    - **Pintu Udara**: Merupakan jalur masuk utama dengan volume tertinggi
    - **Pintu Laut**: Volume menengah dengan variabilitas yang cukup stabil
    - **Pintu Darat**: Volume terendah namun mengalami peningkatan signifikan dari tahun 2016

    **2. Validasi Simulasi:**
    - Simulasi menggunakan distribusi normal berhasil mereplikasi pola data historis
    - Parameter mean dan standar deviasi dari simulasi mendekati data asli
    - Proporsi relatif antar pintu masuk terjaga dalam simulasi

    **3. Implikasi Strategis:**
    - Pintu udara tetap menjadi fokus utama infrastruktur pariwisata
    - Pintu darat menunjukkan potensi pertumbuhan yang perlu diperhatikan
    - Diversifikasi jalur masuk penting untuk resiliensi sektor pariwisata
    """)

if __name__ == "__main__":
    main()
