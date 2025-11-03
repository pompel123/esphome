from esphome.components import climate
import esphome.codegen as cg
import esphome.config_validation as cv

# Namespace and class definition
mill_panelheater_gen2_ns = cg.esphome_ns.namespace("mill_panelheater_gen2")
MillPanelHeaterGen2 = mill_panelheater_gen2_ns.class_(
    "MillPanelHeaterGen2", climate.Climate, cg.Component
)

# Define schema (new-style, no GenerateID)
CONFIG_SCHEMA = climate.climate_schema(MillPanelHeaterGen2).extend(cv.COMPONENT_SCHEMA)

# Register the component and climate
async def to_code(config):
    var = cg.new_Pvariable("mill_panelheater_gen2", MillPanelHeaterGen2)
    await cg.register_component(var, config)
    await climate.register_climate(var, config)
