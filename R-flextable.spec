#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-flextable
Version  : 0.8.2
Release  : 11
URL      : https://cran.r-project.org/src/contrib/flextable_0.8.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/flextable_0.8.2.tar.gz
Summary  : Functions for Tabular Reporting
Group    : Development/Tools
License  : GPL-3.0
Requires: R-base64enc
Requires: R-data.table
Requires: R-gdtools
Requires: R-htmltools
Requires: R-knitr
Requires: R-officer
Requires: R-rlang
Requires: R-rmarkdown
Requires: R-uuid
Requires: R-xml2
BuildRequires : R-base64enc
BuildRequires : R-data.table
BuildRequires : R-gdtools
BuildRequires : R-htmltools
BuildRequires : R-knitr
BuildRequires : R-officer
BuildRequires : R-rlang
BuildRequires : R-rmarkdown
BuildRequires : R-uuid
BuildRequires : R-xml2
BuildRequires : buildreq-R

%description
documents from 'R Markdown' and as 'Grid Graphics' objects. Functions are provided to let users 
  create tables, modify and format their content. It also extends package 'officer' that does 
  not contain any feature for customized tabular reporting.

%prep
%setup -q -n flextable
cd %{_builddir}/flextable

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664289945

%install
export SOURCE_DATE_EPOCH=1664289945
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/flextable/DESCRIPTION
/usr/lib64/R/library/flextable/INDEX
/usr/lib64/R/library/flextable/Meta/Rd.rds
/usr/lib64/R/library/flextable/Meta/features.rds
/usr/lib64/R/library/flextable/Meta/hsearch.rds
/usr/lib64/R/library/flextable/Meta/links.rds
/usr/lib64/R/library/flextable/Meta/nsInfo.rds
/usr/lib64/R/library/flextable/Meta/package.rds
/usr/lib64/R/library/flextable/Meta/vignette.rds
/usr/lib64/R/library/flextable/NAMESPACE
/usr/lib64/R/library/flextable/NEWS.md
/usr/lib64/R/library/flextable/R/flextable
/usr/lib64/R/library/flextable/R/flextable.rdb
/usr/lib64/R/library/flextable/R/flextable.rdx
/usr/lib64/R/library/flextable/doc/index.html
/usr/lib64/R/library/flextable/doc/overview.Rmd
/usr/lib64/R/library/flextable/doc/overview.html
/usr/lib64/R/library/flextable/examples/rmd/captions_example.Rmd
/usr/lib64/R/library/flextable/examples/rmd/demo.Rmd
/usr/lib64/R/library/flextable/examples/rmd/loop_with_flextable.Rmd
/usr/lib64/R/library/flextable/flextablelogo.svg
/usr/lib64/R/library/flextable/help/AnIndex
/usr/lib64/R/library/flextable/help/aliases.rds
/usr/lib64/R/library/flextable/help/figures/fig_add_footer_1.png
/usr/lib64/R/library/flextable/help/figures/fig_add_footer_lines_1.png
/usr/lib64/R/library/flextable/help/figures/fig_add_footer_row_1.png
/usr/lib64/R/library/flextable/help/figures/fig_add_header_1.png
/usr/lib64/R/library/flextable/help/figures/fig_add_header_lines_1.png
/usr/lib64/R/library/flextable/help/figures/fig_add_header_row_1.png
/usr/lib64/R/library/flextable/help/figures/fig_align_1.png
/usr/lib64/R/library/flextable/help/figures/fig_append_chunks_1.png
/usr/lib64/R/library/flextable/help/figures/fig_as_b_1.png
/usr/lib64/R/library/flextable/help/figures/fig_as_bracket_1.png
/usr/lib64/R/library/flextable/help/figures/fig_as_chunk_1.png
/usr/lib64/R/library/flextable/help/figures/fig_as_flextable.gam_1.png
/usr/lib64/R/library/flextable/help/figures/fig_as_flextable.glm_1.png
/usr/lib64/R/library/flextable/help/figures/fig_as_flextable.grouped_data_1.png
/usr/lib64/R/library/flextable/help/figures/fig_as_flextable.htest_1.png
/usr/lib64/R/library/flextable/help/figures/fig_as_flextable.lm_1.png
/usr/lib64/R/library/flextable/help/figures/fig_as_flextable.xtable_1.png
/usr/lib64/R/library/flextable/help/figures/fig_as_flextable.xtable_2.png
/usr/lib64/R/library/flextable/help/figures/fig_as_flextable.xtable_3.png
/usr/lib64/R/library/flextable/help/figures/fig_as_i_1.png
/usr/lib64/R/library/flextable/help/figures/fig_as_image_1.png
/usr/lib64/R/library/flextable/help/figures/fig_as_paragraph_1.png
/usr/lib64/R/library/flextable/help/figures/fig_as_sub_1.png
/usr/lib64/R/library/flextable/help/figures/fig_as_sup_1.png
/usr/lib64/R/library/flextable/help/figures/fig_autofit_1.png
/usr/lib64/R/library/flextable/help/figures/fig_autofit_2.png
/usr/lib64/R/library/flextable/help/figures/fig_bg_1.png
/usr/lib64/R/library/flextable/help/figures/fig_bg_2.png
/usr/lib64/R/library/flextable/help/figures/fig_bold_1.png
/usr/lib64/R/library/flextable/help/figures/fig_border_inner_1.png
/usr/lib64/R/library/flextable/help/figures/fig_border_inner_h_1.png
/usr/lib64/R/library/flextable/help/figures/fig_border_inner_v_1.png
/usr/lib64/R/library/flextable/help/figures/fig_border_outer_1.png
/usr/lib64/R/library/flextable/help/figures/fig_border_remove_1.png
/usr/lib64/R/library/flextable/help/figures/fig_border_remove_2.png
/usr/lib64/R/library/flextable/help/figures/fig_colformat_double_1.png
/usr/lib64/R/library/flextable/help/figures/fig_colformat_image_1.png
/usr/lib64/R/library/flextable/help/figures/fig_colformat_num_1.png
/usr/lib64/R/library/flextable/help/figures/fig_color_1.png
/usr/lib64/R/library/flextable/help/figures/fig_color_2.png
/usr/lib64/R/library/flextable/help/figures/fig_compose_1.png
/usr/lib64/R/library/flextable/help/figures/fig_compose_2.png
/usr/lib64/R/library/flextable/help/figures/fig_continuous_summary_1.png
/usr/lib64/R/library/flextable/help/figures/fig_delete_part_1.png
/usr/lib64/R/library/flextable/help/figures/fig_fit_to_width_1.png
/usr/lib64/R/library/flextable/help/figures/fig_fit_to_width_2.png
/usr/lib64/R/library/flextable/help/figures/fig_font_1.png
/usr/lib64/R/library/flextable/help/figures/fig_font_2.png
/usr/lib64/R/library/flextable/help/figures/fig_fontsize_1.png
/usr/lib64/R/library/flextable/help/figures/fig_footnote_1.png
/usr/lib64/R/library/flextable/help/figures/fig_footnote_2.png
/usr/lib64/R/library/flextable/help/figures/fig_formats.png
/usr/lib64/R/library/flextable/help/figures/fig_gg_chunk_1.png
/usr/lib64/R/library/flextable/help/figures/fig_height_1.png
/usr/lib64/R/library/flextable/help/figures/fig_height_2.png
/usr/lib64/R/library/flextable/help/figures/fig_highlight_1.png
/usr/lib64/R/library/flextable/help/figures/fig_hline_1.png
/usr/lib64/R/library/flextable/help/figures/fig_hline_bottom_1.png
/usr/lib64/R/library/flextable/help/figures/fig_hline_top_1.png
/usr/lib64/R/library/flextable/help/figures/fig_hrule_1.png
/usr/lib64/R/library/flextable/help/figures/fig_hrule_2.png
/usr/lib64/R/library/flextable/help/figures/fig_italic_1.png
/usr/lib64/R/library/flextable/help/figures/fig_line_spacing_1.png
/usr/lib64/R/library/flextable/help/figures/fig_lollipop_1.png
/usr/lib64/R/library/flextable/help/figures/fig_merge_h_range_1.png
/usr/lib64/R/library/flextable/help/figures/fig_merge_none_1.png
/usr/lib64/R/library/flextable/help/figures/fig_merge_v_1.png
/usr/lib64/R/library/flextable/help/figures/fig_merge_v_2.png
/usr/lib64/R/library/flextable/help/figures/fig_minibar_1.png
/usr/lib64/R/library/flextable/help/figures/fig_padding_1.png
/usr/lib64/R/library/flextable/help/figures/fig_plot_chunk_1.png
/usr/lib64/R/library/flextable/help/figures/fig_rotate_1.png
/usr/lib64/R/library/flextable/help/figures/fig_separate_header_1.png
/usr/lib64/R/library/flextable/help/figures/fig_set_flextable_defaults_1.png
/usr/lib64/R/library/flextable/help/figures/fig_set_flextable_defaults_2.png
/usr/lib64/R/library/flextable/help/figures/fig_set_header_footer_df_1.png
/usr/lib64/R/library/flextable/help/figures/fig_set_header_footer_df_2.png
/usr/lib64/R/library/flextable/help/figures/fig_set_header_labels_1.png
/usr/lib64/R/library/flextable/help/figures/fig_set_table_properties_1.png
/usr/lib64/R/library/flextable/help/figures/fig_set_table_properties_2.png
/usr/lib64/R/library/flextable/help/figures/fig_set_table_properties_3.png
/usr/lib64/R/library/flextable/help/figures/fig_style_1.png
/usr/lib64/R/library/flextable/help/figures/fig_summarizor_1.png
/usr/lib64/R/library/flextable/help/figures/fig_summarizor_2.png
/usr/lib64/R/library/flextable/help/figures/fig_tabulator_1.png
/usr/lib64/R/library/flextable/help/figures/fig_tabulator_2.png
/usr/lib64/R/library/flextable/help/figures/fig_theme_alafoli_1.png
/usr/lib64/R/library/flextable/help/figures/fig_theme_apa_1.png
/usr/lib64/R/library/flextable/help/figures/fig_theme_booktabs_1.png
/usr/lib64/R/library/flextable/help/figures/fig_theme_box_1.png
/usr/lib64/R/library/flextable/help/figures/fig_theme_tron_1.png
/usr/lib64/R/library/flextable/help/figures/fig_theme_tron_legacy_1.png
/usr/lib64/R/library/flextable/help/figures/fig_theme_vader_1.png
/usr/lib64/R/library/flextable/help/figures/fig_theme_vanilla_1.png
/usr/lib64/R/library/flextable/help/figures/fig_theme_zebra_1.png
/usr/lib64/R/library/flextable/help/figures/fig_valign_1.png
/usr/lib64/R/library/flextable/help/figures/fig_valign_2.png
/usr/lib64/R/library/flextable/help/figures/fig_vline_1.png
/usr/lib64/R/library/flextable/help/figures/fig_vline_left_1.png
/usr/lib64/R/library/flextable/help/figures/fig_vline_right_1.png
/usr/lib64/R/library/flextable/help/figures/fig_width_1.png
/usr/lib64/R/library/flextable/help/figures/flextable_functions.png
/usr/lib64/R/library/flextable/help/figures/logo.png
/usr/lib64/R/library/flextable/help/flextable.rdb
/usr/lib64/R/library/flextable/help/flextable.rdx
/usr/lib64/R/library/flextable/help/paths.rds
/usr/lib64/R/library/flextable/html/00Index.html
/usr/lib64/R/library/flextable/html/R.css
/usr/lib64/R/library/flextable/tests/testthat.R
/usr/lib64/R/library/flextable/tests/testthat/_snaps/borders/docx-borders.png
/usr/lib64/R/library/flextable/tests/testthat/_snaps/borders/html-borders.png
/usr/lib64/R/library/flextable/tests/testthat/_snaps/borders/pptx-borders.png
/usr/lib64/R/library/flextable/tests/testthat/_snaps/md-captions/bookdown_html_document2.png
/usr/lib64/R/library/flextable/tests/testthat/_snaps/md-captions/bookdown_pdf_document2.png
/usr/lib64/R/library/flextable/tests/testthat/_snaps/md-captions/bookdown_word_document2.png
/usr/lib64/R/library/flextable/tests/testthat/_snaps/md-captions/officedown_word_document2.png
/usr/lib64/R/library/flextable/tests/testthat/_snaps/md-captions/rmarkdown_html_document.png
/usr/lib64/R/library/flextable/tests/testthat/_snaps/md-captions/rmarkdown_pdf_document.png
/usr/lib64/R/library/flextable/tests/testthat/_snaps/md-captions/rmarkdown_word_document.png
/usr/lib64/R/library/flextable/tests/testthat/rmd/bookdown.Rmd
/usr/lib64/R/library/flextable/tests/testthat/rmd/captions.Rmd
/usr/lib64/R/library/flextable/tests/testthat/rmd/rmarkdown.Rmd
/usr/lib64/R/library/flextable/tests/testthat/test-borders.R
/usr/lib64/R/library/flextable/tests/testthat/test-captions-rmd.R
/usr/lib64/R/library/flextable/tests/testthat/test-cell-content.R
/usr/lib64/R/library/flextable/tests/testthat/test-dimensions.R
/usr/lib64/R/library/flextable/tests/testthat/test-errors.R
/usr/lib64/R/library/flextable/tests/testthat/test-footers.R
/usr/lib64/R/library/flextable/tests/testthat/test-footnote.R
/usr/lib64/R/library/flextable/tests/testthat/test-headers.R
/usr/lib64/R/library/flextable/tests/testthat/test-images.R
/usr/lib64/R/library/flextable/tests/testthat/test-latex.R
/usr/lib64/R/library/flextable/tests/testthat/test-link.R
/usr/lib64/R/library/flextable/tests/testthat/test-md-captions.R
/usr/lib64/R/library/flextable/tests/testthat/test-merge.R
/usr/lib64/R/library/flextable/tests/testthat/test-misc.R
/usr/lib64/R/library/flextable/tests/testthat/test-padding.R
/usr/lib64/R/library/flextable/tests/testthat/test-pptx-tables.R
/usr/lib64/R/library/flextable/tests/testthat/test-proc-freq.R
/usr/lib64/R/library/flextable/tests/testthat/test-rotations.R
/usr/lib64/R/library/flextable/tests/testthat/test-styles.R
/usr/lib64/R/library/flextable/tests/testthat/test-text.R
/usr/lib64/R/library/flextable/tests/testthat/to-img.R
/usr/lib64/R/library/flextable/tests/testthat/zzzzz.R
/usr/lib64/R/library/flextable/web_1.1.0/scrool.css
/usr/lib64/R/library/flextable/web_1.1.0/tabwid.css
