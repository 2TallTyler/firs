"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryOrganic, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryOrganic(id='vineyard',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='86',
                    prob_in_game='3',
                    prob_random='10',
                    prospect_chance='0.75',
                    name='string(STR_IND_VINEYARD)',
                    layouts='[vineyard_tilelayout_1, vineyard_tilelayout_2, vineyard_tilelayout_3, vineyard_tilelayout_4, vineyard_tilelayout_5]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(require_cluster=['vineyard', [20, 72, 1, 4]]),
                    prod_cargo_types=['BEER', 'FRUT'],
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_PLANTATION))',
                    fund_cost_multiplier='54',
                    prod_multiplier='[11, 8]',
                    substitute='0',
                    template="refactor_vineyard.pypnml" )

industry.economy_variations['BASIC_TROPIC'].enabled = True
industry.economy_variations['BASIC_TROPIC'].prod_multiplier = '[9, 9]'

building_0 = industry.add_sprite(
    sprite_number = 1633,
    xoffset = 2,
    yoffset = 2,
    xextent = 13,
    yextent = 13,
)
building_1 = industry.add_sprite(
    sprite_number = 1689,
    xoffset = 8,
    yoffset = 2,
    xextent = 7,
    yextent = 13,
)
building_2 = industry.add_sprite(
    sprite_number = 1620,
    yoffset = 7,
    yextent = 8,
)
building_3 = industry.add_sprite(
    sprite_number = 1633,
    xoffset = 8,
    yoffset = 7,
    xextent = 7,
    yextent = 8,
)
building_4 = industry.add_sprite(
    sprite_number = 1620,
    xoffset = 2,
    yoffset = 2,
    xextent = 13,
    yextent = 13,
)
building_5 = industry.add_sprite(
    sprite_number = 1633,
    yoffset = 7,
    yextent = 8,
)
building_6 = industry.add_sprite(
    sprite_number = 1620,
    xoffset = 8,
    yoffset = 7,
    xextent = 7,
    yextent = 8,
)
building_7 = industry.add_sprite(
    sprite_number = 1633,
    xoffset = 8,
    yoffset = 2,
    xextent = 7,
    yextent = 13,
)
building_8 = industry.add_sprite(
    sprite_number = 1689,
    xoffset = 8,
    yoffset = 7,
    xextent = 7,
    yextent = 8,
)
building_9 = industry.add_sprite(
    sprite_number = 1689,
    xoffset = 2,
    yoffset = 2,
    xextent = 13,
    yextent = 13,
)
building_10 = industry.add_sprite(
    sprite_number = 1620,
    xoffset = 8,
    yoffset = 2,
    xextent = 7,
    yextent = 13,
)
building_11 = industry.add_sprite(
    sprite_number = 1689,
    yoffset = 7,
    yextent = 8,
)
building_12 = industry.add_sprite(
    sprite_number = 1758,
    xoffset = 2,
    yoffset = 2,
    xextent = 13,
    yextent = 13,
)
building_13 = industry.add_sprite(
    sprite_number = 1759,
    xoffset = 8,
    yoffset = 2,
    xextent = 7,
    yextent = 13,
)
building_14 = industry.add_sprite(
    sprite_number = 1759,
    yoffset = 7,
    yextent = 8,
)
building_15 = industry.add_sprite(
    sprite_number = 1758,
    xoffset = 8,
    yoffset = 7,
    xextent = 7,
    yextent = 8,
)
building_16 = industry.add_sprite(
    sprite_number = 1759,
    xoffset = 2,
    yoffset = 2,
    xextent = 13,
    yextent = 13,
)
building_17 = industry.add_sprite(
    sprite_number = 1758,
    yoffset = 7,
    yextent = 8,
)
building_18 = industry.add_sprite(
    sprite_number = 1759,
    xoffset = 8,
    yoffset = 7,
    xextent = 7,
    yextent = 8,
)
building_19 = industry.add_sprite(
    sprite_number = 1758,
    xoffset = 8,
    yoffset = 2,
    xextent = 7,
    yextent = 13,
)
building_20 = industry.add_sprite(
    sprite_number = 1863,
    xoffset = 2,
    yoffset = 2,
    xextent = 13,
    yextent = 13,
)
building_21 = industry.add_sprite(
    sprite_number = 1863,
    xoffset = 8,
    yoffset = 2,
    xextent = 7,
    yextent = 13,
)
building_22 = industry.add_sprite(
    sprite_number = 1863,
    yoffset = 7,
    yextent = 8,
)
building_23 = industry.add_sprite(
    sprite_number = 1863,
    xoffset = 8,
    yoffset = 7,
    xextent = 7,
    yextent = 8,
)
building_24 = industry.add_sprite(
    sprite_number = 1863,
    xoffset = 2,
    yoffset = 2,
    xextent = 13,
    yextent = 13,
)
building_25 = industry.add_sprite(
    sprite_number = 1863,
    yoffset = 7,
    yextent = 8,
)
building_26 = industry.add_sprite(
    sprite_number = 1863,
    xoffset = 8,
    yoffset = 7,
    xextent = 7,
    yextent = 8,
)
building_27 = industry.add_sprite(
    sprite_number = 1863,
    xoffset = 8,
    yoffset = 2,
    xextent = 7,
    yextent = 13,
)
building_28 = industry.add_sprite(
    sprite_number = 1863,
    xoffset = 8,
    yoffset = 7,
    xextent = 7,
    yextent = 8,
)
building_29 = industry.add_sprite(
    sprite_number = 1863,
    xoffset = 2,
    yoffset = 2,
    xextent = 13,
    yextent = 13,
)
building_30 = industry.add_sprite(
    sprite_number = 1863,
    xoffset = 8,
    yoffset = 2,
    xextent = 7,
    yextent = 13,
)
building_31 = industry.add_sprite(
    sprite_number = 1863,
    yoffset = 7,
    yextent = 8,
)

sprite_ground_4145 = industry.add_sprite(
    sprite_number = 4145
)
sprite_ground_4146 = industry.add_sprite(
    sprite_number = 4146
)
sprite_ground_4147 = industry.add_sprite(
    sprite_number = 4147
)
sprite_ground_4148 = industry.add_sprite(
    sprite_number = 4148
)
sprite_ground_4149 = industry.add_sprite(
    sprite_number = 4149
)
sprite_ground_4150 = industry.add_sprite(
    sprite_number = 4150
)
sprite_ground_4151 = industry.add_sprite(
    sprite_number = 4151
)
sprite_ground_4152 = industry.add_sprite(
    sprite_number = 4152
)
sprite_ground_4153 = industry.add_sprite(
    sprite_number = 4153
)
sprite_ground_4154 = industry.add_sprite(
    sprite_number = 4154
)
sprite_ground_4155 = industry.add_sprite(
    sprite_number = 4155
)
sprite_ground_4156 = industry.add_sprite(
    sprite_number = 4156
)
sprite_ground_4157 = industry.add_sprite(
    sprite_number = 4157
)
sprite_ground_4158 = industry.add_sprite(
    sprite_number = 4158
)
sprite_ground_4159 = industry.add_sprite(
    sprite_number = 4159
)
sprite_ground_4160 = industry.add_sprite(
    sprite_number = 4160
)
sprite_ground_4161 = industry.add_sprite(
    sprite_number = 4161
)
sprite_ground_4162 = industry.add_sprite(
    sprite_number = 4162
)
sprite_ground_4163 = industry.add_sprite(
    sprite_number = 4163
)

sprite_ground_4164 = industry.add_sprite(
    sprite_number = 4164
)
sprite_ground_4165 = industry.add_sprite(
    sprite_number = 4165
)
sprite_ground_4166 = industry.add_sprite(
    sprite_number = 4166
)
sprite_ground_4167 = industry.add_sprite(
    sprite_number = 4167
)
sprite_ground_4168 = industry.add_sprite(
    sprite_number = 4168
)
sprite_ground_4169 = industry.add_sprite(
    sprite_number = 4169
)
sprite_ground_4170 = industry.add_sprite(
    sprite_number = 4170
)
sprite_ground_4171 = industry.add_sprite(
    sprite_number = 4171
)
sprite_ground_4172 = industry.add_sprite(
    sprite_number = 4172
)
sprite_ground_4173 = industry.add_sprite(
    sprite_number = 4173
)
sprite_ground_4174 = industry.add_sprite(
    sprite_number = 4174
)
sprite_ground_4175 = industry.add_sprite(
    sprite_number = 4175
)
sprite_ground_4176 = industry.add_sprite(
    sprite_number = 4176
)
sprite_ground_4177 = industry.add_sprite(
    sprite_number = 4177
)
sprite_ground_4178 = industry.add_sprite(
    sprite_number = 4178
)
sprite_ground_4179 = industry.add_sprite(
    sprite_number = 4179
)
sprite_ground_4180 = industry.add_sprite(
    sprite_number = 4180
)
sprite_ground_4181 = industry.add_sprite(
    sprite_number = 4181
)
sprite_ground_4182 = industry.add_sprite(
    sprite_number = 4182
)

industry.add_spritelayout(
    id = 'vineyard_597',
    ground_sprite = sprite_ground_4164,
    ground_overlay = sprite_ground_4164,
    building_sprites = [building_0, building_1, building_2, building_3],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_598',
    ground_sprite = sprite_ground_4165,
    ground_overlay = sprite_ground_4165,
    building_sprites = [building_4, building_1, building_5, building_6],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_599',
    ground_sprite = sprite_ground_4166,
    ground_overlay = sprite_ground_4166,
    building_sprites = [building_0, building_7, building_2, building_8],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_600',
    ground_sprite = sprite_ground_4167,
    ground_overlay = sprite_ground_4167,
    building_sprites = [building_9, building_10, building_5, building_6],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_601',
    ground_sprite = sprite_ground_4168,
    ground_overlay = sprite_ground_4168,
    building_sprites = [building_0, building_10, building_5, building_8],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_602',
    ground_sprite = sprite_ground_4169,
    ground_overlay = sprite_ground_4169,
    building_sprites = [building_4, building_7, building_11, building_6],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_603',
    ground_sprite = sprite_ground_4170,
    ground_overlay = sprite_ground_4170,
    building_sprites = [building_9, building_10, building_5, building_3],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_604',
    ground_sprite = sprite_ground_4171,
    ground_overlay = sprite_ground_4171,
    building_sprites = [building_4, building_1, building_2, building_3],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_605',
    ground_sprite = sprite_ground_4172,
    ground_overlay = sprite_ground_4172,
    building_sprites = [building_0, building_10, building_11, building_6],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_606',
    ground_sprite = sprite_ground_4173,
    ground_overlay = sprite_ground_4173,
    building_sprites = [building_0, building_10, building_2, building_8],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_607',
    ground_sprite = sprite_ground_4174,
    ground_overlay = sprite_ground_4174,
    building_sprites = [building_4, building_1, building_5, building_6],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_608',
    ground_sprite = sprite_ground_4175,
    ground_overlay = sprite_ground_4175,
    building_sprites = [building_4, building_10, building_2, building_8],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_609',
    ground_sprite = sprite_ground_4176,
    ground_overlay = sprite_ground_4176,
    building_sprites = [building_0, building_10, building_2, building_8],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_610',
    ground_sprite = sprite_ground_4177,
    ground_overlay = sprite_ground_4177,
    building_sprites = [building_4, building_1, building_5, building_6],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_611',
    ground_sprite = sprite_ground_4178,
    ground_overlay = sprite_ground_4178,
    building_sprites = [building_4, building_1, building_5, building_6],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_612',
    ground_sprite = sprite_ground_4179,
    ground_overlay = sprite_ground_4179,
    building_sprites = [building_9, building_7, building_2, building_3],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_613',
    ground_sprite = sprite_ground_4180,
    ground_overlay = sprite_ground_4180,
    building_sprites = [building_0, building_1, building_2, building_6],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_614',
    ground_sprite = sprite_ground_4181,
    ground_overlay = sprite_ground_4181,
    building_sprites = [building_4, building_7, building_2, building_8],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_615',
    ground_sprite = sprite_ground_4182,
    ground_overlay = sprite_ground_4182,
    building_sprites = [building_4, building_10, building_5, building_8],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_620',
    ground_sprite = sprite_ground_4164,
    ground_overlay = sprite_ground_4164,
    building_sprites = [building_12, building_13, building_14, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_621',
    ground_sprite = sprite_ground_4165,
    ground_overlay = sprite_ground_4165,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_622',
    ground_sprite = sprite_ground_4166,
    ground_overlay = sprite_ground_4166,
    building_sprites = [building_12, building_19, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_623',
    ground_sprite = sprite_ground_4167,
    ground_overlay = sprite_ground_4167,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_624',
    ground_sprite = sprite_ground_4168,
    ground_overlay = sprite_ground_4168,
    building_sprites = [building_12, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_625',
    ground_sprite = sprite_ground_4169,
    ground_overlay = sprite_ground_4169,
    building_sprites = [building_16, building_19, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_626',
    ground_sprite = sprite_ground_4170,
    ground_overlay = sprite_ground_4170,
    building_sprites = [building_16, building_13, building_17, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_627',
    ground_sprite = sprite_ground_4171,
    ground_overlay = sprite_ground_4171,
    building_sprites = [building_16, building_13, building_14, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_628',
    ground_sprite = sprite_ground_4172,
    ground_overlay = sprite_ground_4172,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_629',
    ground_sprite = sprite_ground_4173,
    ground_overlay = sprite_ground_4173,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_630',
    ground_sprite = sprite_ground_4174,
    ground_overlay = sprite_ground_4174,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_631',
    ground_sprite = sprite_ground_4175,
    ground_overlay = sprite_ground_4175,
    building_sprites = [building_16, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_632',
    ground_sprite = sprite_ground_4176,
    ground_overlay = sprite_ground_4176,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_633',
    ground_sprite = sprite_ground_4177,
    ground_overlay = sprite_ground_4177,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_634',
    ground_sprite = sprite_ground_4178,
    ground_overlay = sprite_ground_4178,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_635',
    ground_sprite = sprite_ground_4179,
    ground_overlay = sprite_ground_4179,
    building_sprites = [building_16, building_19, building_14, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_636',
    ground_sprite = sprite_ground_4180,
    ground_overlay = sprite_ground_4180,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_637',
    ground_sprite = sprite_ground_4181,
    ground_overlay = sprite_ground_4181,
    building_sprites = [building_16, building_19, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_638',
    ground_sprite = sprite_ground_4182,
    ground_overlay = sprite_ground_4182,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_642',
    ground_sprite = sprite_ground_4164,
    ground_overlay = sprite_ground_4164,
    building_sprites = [building_12, building_13, building_14, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_643',
    ground_sprite = sprite_ground_4165,
    ground_overlay = sprite_ground_4165,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_644',
    ground_sprite = sprite_ground_4166,
    ground_overlay = sprite_ground_4166,
    building_sprites = [building_12, building_19, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_645',
    ground_sprite = sprite_ground_4167,
    ground_overlay = sprite_ground_4167,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_646',
    ground_sprite = sprite_ground_4168,
    ground_overlay = sprite_ground_4168,
    building_sprites = [building_12, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_647',
    ground_sprite = sprite_ground_4169,
    ground_overlay = sprite_ground_4169,
    building_sprites = [building_16, building_19, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_648',
    ground_sprite = sprite_ground_4170,
    ground_overlay = sprite_ground_4170,
    building_sprites = [building_16, building_13, building_17, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_649',
    ground_sprite = sprite_ground_4171,
    ground_overlay = sprite_ground_4171,
    building_sprites = [building_16, building_13, building_14, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_650',
    ground_sprite = sprite_ground_4172,
    ground_overlay = sprite_ground_4172,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_651',
    ground_sprite = sprite_ground_4173,
    ground_overlay = sprite_ground_4173,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_652',
    ground_sprite = sprite_ground_4174,
    ground_overlay = sprite_ground_4174,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_653',
    ground_sprite = sprite_ground_4175,
    ground_overlay = sprite_ground_4175,
    building_sprites = [building_16, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_654',
    ground_sprite = sprite_ground_4176,
    ground_overlay = sprite_ground_4176,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_655',
    ground_sprite = sprite_ground_4177,
    ground_overlay = sprite_ground_4177,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_656',
    ground_sprite = sprite_ground_4178,
    ground_overlay = sprite_ground_4178,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_657',
    ground_sprite = sprite_ground_4179,
    ground_overlay = sprite_ground_4179,
    building_sprites = [building_16, building_19, building_14, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_658',
    ground_sprite = sprite_ground_4180,
    ground_overlay = sprite_ground_4180,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_659',
    ground_sprite = sprite_ground_4181,
    ground_overlay = sprite_ground_4181,
    building_sprites = [building_16, building_19, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_660',
    ground_sprite = sprite_ground_4182,
    ground_overlay = sprite_ground_4182,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_664',
    ground_sprite = sprite_ground_4164,
    ground_overlay = sprite_ground_4164,
    building_sprites = [building_12, building_13, building_14, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_665',
    ground_sprite = sprite_ground_4165,
    ground_overlay = sprite_ground_4165,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_666',
    ground_sprite = sprite_ground_4166,
    ground_overlay = sprite_ground_4166,
    building_sprites = [building_12, building_19, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_667',
    ground_sprite = sprite_ground_4167,
    ground_overlay = sprite_ground_4167,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_668',
    ground_sprite = sprite_ground_4168,
    ground_overlay = sprite_ground_4168,
    building_sprites = [building_12, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_669',
    ground_sprite = sprite_ground_4169,
    ground_overlay = sprite_ground_4169,
    building_sprites = [building_16, building_19, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_670',
    ground_sprite = sprite_ground_4170,
    ground_overlay = sprite_ground_4170,
    building_sprites = [building_16, building_13, building_17, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_671',
    ground_sprite = sprite_ground_4171,
    ground_overlay = sprite_ground_4171,
    building_sprites = [building_16, building_13, building_14, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_672',
    ground_sprite = sprite_ground_4172,
    ground_overlay = sprite_ground_4172,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_673',
    ground_sprite = sprite_ground_4173,
    ground_overlay = sprite_ground_4173,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_674',
    ground_sprite = sprite_ground_4174,
    ground_overlay = sprite_ground_4174,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_675',
    ground_sprite = sprite_ground_4175,
    ground_overlay = sprite_ground_4175,
    building_sprites = [building_16, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_676',
    ground_sprite = sprite_ground_4176,
    ground_overlay = sprite_ground_4176,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_677',
    ground_sprite = sprite_ground_4177,
    ground_overlay = sprite_ground_4177,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_678',
    ground_sprite = sprite_ground_4178,
    ground_overlay = sprite_ground_4178,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_679',
    ground_sprite = sprite_ground_4179,
    ground_overlay = sprite_ground_4179,
    building_sprites = [building_16, building_19, building_14, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_680',
    ground_sprite = sprite_ground_4180,
    ground_overlay = sprite_ground_4180,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_681',
    ground_sprite = sprite_ground_4181,
    ground_overlay = sprite_ground_4181,
    building_sprites = [building_16, building_19, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_682',
    ground_sprite = sprite_ground_4182,
    ground_overlay = sprite_ground_4182,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_686',
    ground_sprite = sprite_ground_4164,
    ground_overlay = sprite_ground_4164,
    building_sprites = [building_12, building_13, building_14, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_687',
    ground_sprite = sprite_ground_4165,
    ground_overlay = sprite_ground_4165,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_688',
    ground_sprite = sprite_ground_4166,
    ground_overlay = sprite_ground_4166,
    building_sprites = [building_12, building_19, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_689',
    ground_sprite = sprite_ground_4167,
    ground_overlay = sprite_ground_4167,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_690',
    ground_sprite = sprite_ground_4168,
    ground_overlay = sprite_ground_4168,
    building_sprites = [building_12, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_691',
    ground_sprite = sprite_ground_4169,
    ground_overlay = sprite_ground_4169,
    building_sprites = [building_16, building_19, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_692',
    ground_sprite = sprite_ground_4170,
    ground_overlay = sprite_ground_4170,
    building_sprites = [building_16, building_13, building_17, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_693',
    ground_sprite = sprite_ground_4171,
    ground_overlay = sprite_ground_4171,
    building_sprites = [building_16, building_13, building_14, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_694',
    ground_sprite = sprite_ground_4172,
    ground_overlay = sprite_ground_4172,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_695',
    ground_sprite = sprite_ground_4173,
    ground_overlay = sprite_ground_4173,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_696',
    ground_sprite = sprite_ground_4174,
    ground_overlay = sprite_ground_4174,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_697',
    ground_sprite = sprite_ground_4175,
    ground_overlay = sprite_ground_4175,
    building_sprites = [building_16, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_698',
    ground_sprite = sprite_ground_4176,
    ground_overlay = sprite_ground_4176,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_699',
    ground_sprite = sprite_ground_4177,
    ground_overlay = sprite_ground_4177,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_700',
    ground_sprite = sprite_ground_4178,
    ground_overlay = sprite_ground_4178,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_701',
    ground_sprite = sprite_ground_4179,
    ground_overlay = sprite_ground_4179,
    building_sprites = [building_16, building_19, building_14, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_702',
    ground_sprite = sprite_ground_4180,
    ground_overlay = sprite_ground_4180,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_703',
    ground_sprite = sprite_ground_4181,
    ground_overlay = sprite_ground_4181,
    building_sprites = [building_16, building_19, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_704',
    ground_sprite = sprite_ground_4182,
    ground_overlay = sprite_ground_4182,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_708',
    ground_sprite = sprite_ground_4164,
    ground_overlay = sprite_ground_4164,
    building_sprites = [building_12, building_13, building_14, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_709',
    ground_sprite = sprite_ground_4165,
    ground_overlay = sprite_ground_4165,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_710',
    ground_sprite = sprite_ground_4166,
    ground_overlay = sprite_ground_4166,
    building_sprites = [building_12, building_19, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_711',
    ground_sprite = sprite_ground_4167,
    ground_overlay = sprite_ground_4167,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_712',
    ground_sprite = sprite_ground_4168,
    ground_overlay = sprite_ground_4168,
    building_sprites = [building_12, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_713',
    ground_sprite = sprite_ground_4169,
    ground_overlay = sprite_ground_4169,
    building_sprites = [building_16, building_19, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_714',
    ground_sprite = sprite_ground_4170,
    ground_overlay = sprite_ground_4170,
    building_sprites = [building_16, building_13, building_17, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_715',
    ground_sprite = sprite_ground_4171,
    ground_overlay = sprite_ground_4171,
    building_sprites = [building_16, building_13, building_14, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_716',
    ground_sprite = sprite_ground_4172,
    ground_overlay = sprite_ground_4172,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_717',
    ground_sprite = sprite_ground_4173,
    ground_overlay = sprite_ground_4173,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_718',
    ground_sprite = sprite_ground_4174,
    ground_overlay = sprite_ground_4174,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_719',
    ground_sprite = sprite_ground_4175,
    ground_overlay = sprite_ground_4175,
    building_sprites = [building_16, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_720',
    ground_sprite = sprite_ground_4176,
    ground_overlay = sprite_ground_4176,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_721',
    ground_sprite = sprite_ground_4177,
    ground_overlay = sprite_ground_4177,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_722',
    ground_sprite = sprite_ground_4178,
    ground_overlay = sprite_ground_4178,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_723',
    ground_sprite = sprite_ground_4179,
    ground_overlay = sprite_ground_4179,
    building_sprites = [building_16, building_19, building_14, building_15],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_724',
    ground_sprite = sprite_ground_4180,
    ground_overlay = sprite_ground_4180,
    building_sprites = [building_12, building_13, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_725',
    ground_sprite = sprite_ground_4181,
    ground_overlay = sprite_ground_4181,
    building_sprites = [building_16, building_19, building_14, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_726',
    ground_sprite = sprite_ground_4182,
    ground_overlay = sprite_ground_4182,
    building_sprites = [building_16, building_13, building_17, building_18],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_731',
    ground_sprite = sprite_ground_4145,
    ground_overlay = sprite_ground_4145,
    building_sprites = [building_20, building_21, building_22, building_23],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_732',
    ground_sprite = sprite_ground_4146,
    ground_overlay = sprite_ground_4146,
    building_sprites = [building_24, building_21, building_25, building_26],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_733',
    ground_sprite = sprite_ground_4147,
    ground_overlay = sprite_ground_4147,
    building_sprites = [building_20, building_27, building_22, building_28],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_734',
    ground_sprite = sprite_ground_4148,
    ground_overlay = sprite_ground_4148,
    building_sprites = [building_29, building_30, building_25, building_26],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_735',
    ground_sprite = sprite_ground_4149,
    ground_overlay = sprite_ground_4149,
    building_sprites = [building_20, building_30, building_25, building_28],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_736',
    ground_sprite = sprite_ground_4150,
    ground_overlay = sprite_ground_4150,
    building_sprites = [building_24, building_27, building_31, building_26],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_737',
    ground_sprite = sprite_ground_4151,
    ground_overlay = sprite_ground_4151,
    building_sprites = [building_29, building_30, building_25, building_23],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_738',
    ground_sprite = sprite_ground_4152,
    ground_overlay = sprite_ground_4152,
    building_sprites = [building_24, building_21, building_22, building_23],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_739',
    ground_sprite = sprite_ground_4153,
    ground_overlay = sprite_ground_4153,
    building_sprites = [building_20, building_30, building_31, building_26],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_740',
    ground_sprite = sprite_ground_4154,
    ground_overlay = sprite_ground_4154,
    building_sprites = [building_20, building_30, building_22, building_28],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_741',
    ground_sprite = sprite_ground_4155,
    ground_overlay = sprite_ground_4155,
    building_sprites = [building_24, building_21, building_25, building_26],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_742',
    ground_sprite = sprite_ground_4156,
    ground_overlay = sprite_ground_4156,
    building_sprites = [building_24, building_30, building_22, building_28],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_743',
    ground_sprite = sprite_ground_4157,
    ground_overlay = sprite_ground_4157,
    building_sprites = [building_20, building_30, building_22, building_28],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_744',
    ground_sprite = sprite_ground_4158,
    ground_overlay = sprite_ground_4158,
    building_sprites = [building_24, building_21, building_25, building_26],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_745',
    ground_sprite = sprite_ground_4159,
    ground_overlay = sprite_ground_4159,
    building_sprites = [building_24, building_21, building_25, building_26],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_746',
    ground_sprite = sprite_ground_4160,
    ground_overlay = sprite_ground_4160,
    building_sprites = [building_29, building_27, building_22, building_23],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_747',
    ground_sprite = sprite_ground_4161,
    ground_overlay = sprite_ground_4161,
    building_sprites = [building_20, building_21, building_22, building_26],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_748',
    ground_sprite = sprite_ground_4162,
    ground_overlay = sprite_ground_4162,
    building_sprites = [building_24, building_27, building_22, building_28],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_749',
    ground_sprite = sprite_ground_4163,
    ground_overlay = sprite_ground_4163,
    building_sprites = [building_24, building_30, building_25, building_28],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_753',
    ground_sprite = sprite_ground_4145,
    ground_overlay = sprite_ground_4145,
    building_sprites = [building_20, building_21, building_22, building_23],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_754',
    ground_sprite = sprite_ground_4146,
    ground_overlay = sprite_ground_4146,
    building_sprites = [building_24, building_21, building_25, building_26],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_755',
    ground_sprite = sprite_ground_4147,
    ground_overlay = sprite_ground_4147,
    building_sprites = [building_20, building_27, building_22, building_28],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_756',
    ground_sprite = sprite_ground_4148,
    ground_overlay = sprite_ground_4148,
    building_sprites = [building_29, building_30, building_25, building_26],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_757',
    ground_sprite = sprite_ground_4149,
    ground_overlay = sprite_ground_4149,
    building_sprites = [building_20, building_30, building_25, building_28],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_758',
    ground_sprite = sprite_ground_4150,
    ground_overlay = sprite_ground_4150,
    building_sprites = [building_24, building_27, building_31, building_26],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_759',
    ground_sprite = sprite_ground_4151,
    ground_overlay = sprite_ground_4151,
    building_sprites = [building_29, building_30, building_25, building_23],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_760',
    ground_sprite = sprite_ground_4152,
    ground_overlay = sprite_ground_4152,
    building_sprites = [building_24, building_21, building_22, building_23],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_761',
    ground_sprite = sprite_ground_4153,
    ground_overlay = sprite_ground_4153,
    building_sprites = [building_20, building_30, building_31, building_26],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_762',
    ground_sprite = sprite_ground_4154,
    ground_overlay = sprite_ground_4154,
    building_sprites = [building_20, building_30, building_22, building_28],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_763',
    ground_sprite = sprite_ground_4155,
    ground_overlay = sprite_ground_4155,
    building_sprites = [building_24, building_21, building_25, building_26],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_764',
    ground_sprite = sprite_ground_4156,
    ground_overlay = sprite_ground_4156,
    building_sprites = [building_24, building_30, building_22, building_28],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_765',
    ground_sprite = sprite_ground_4157,
    ground_overlay = sprite_ground_4157,
    building_sprites = [building_20, building_30, building_22, building_28],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_766',
    ground_sprite = sprite_ground_4158,
    ground_overlay = sprite_ground_4158,
    building_sprites = [building_24, building_21, building_25, building_26],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_767',
    ground_sprite = sprite_ground_4159,
    ground_overlay = sprite_ground_4159,
    building_sprites = [building_24, building_21, building_25, building_26],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_768',
    ground_sprite = sprite_ground_4160,
    ground_overlay = sprite_ground_4160,
    building_sprites = [building_29, building_27, building_22, building_23],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_769',
    ground_sprite = sprite_ground_4161,
    ground_overlay = sprite_ground_4161,
    building_sprites = [building_20, building_21, building_22, building_26],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_770',
    ground_sprite = sprite_ground_4162,
    ground_overlay = sprite_ground_4162,
    building_sprites = [building_24, building_27, building_22, building_28],
    fences = [],
)
industry.add_spritelayout(
    id = 'vineyard_771',
    ground_sprite = sprite_ground_4163,
    ground_overlay = sprite_ground_4163,
    building_sprites = [building_24, building_30, building_25, building_28],
    fences = [],
)

