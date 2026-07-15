from basyx.aas import model
from basyx.aas.adapter import aasx
from LAG14ER_Submodel.nameplate import submodel as nameplate_submodel
from LAG14ER_Submodel.handover import submodel as handover_submodel
from LAG14ER_Submodel.techdata import submodel as techdata_submodel
from LAG14ER_Submodel.carbon import submodel as carbon_submodel
from LAG14ER_Submodel.maintenance import submodel as maintenance_submodel


# create the AAS containing AssetInformation
asset_inforamtion = model.AssetInformation(
    asset_kind=model.AssetKind.TYPE,
    global_asset_id='https://www.afriso.com/de/produkte/haustechnik/leckanzeiger-leckueberwachungssysteme-und-leckschutzauskleidungen/zubehoer-ersatzteile-leckanzeiger-leckueberwachungssysteme-und-leckschutzauskleidungen/lag-14-er/40642-signalteil-lag-14-er'
)

# create the Asset AdministrationShell
# TODO : model.MultiLanguageNameType() need english name?
ass = model.AssetAdministrationShell(
    asset_information=asset_inforamtion,
    id_short='LAG14ER',
    display_name=model.MultiLanguageNameType(
        {"en": "LAG14ER", "de": "LAG14ER"}
    ),
    id_='https://www.afriso.com/aas/LAG14ER',
    description=model.MultiLanguageTextType(
        {"de": "Steuergerät LAG-14 ER / Leckanzeiger"}
    ),
    administration=model.AdministrativeInformation(
        version='1',
        revision='0'
    ),
    submodel={
        model.ModelReference.from_referable(nameplate_submodel),
        model.ModelReference.from_referable(handover_submodel),
        model.ModelReference.from_referable(techdata_submodel),
        model.ModelReference.from_referable(carbon_submodel),
        model.ModelReference.from_referable(maintenance_submodel),
    },
    derived_from=None,
)

# create the Submodel object

print("AAS Environment exported")