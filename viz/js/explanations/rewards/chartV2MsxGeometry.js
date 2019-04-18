function addMsxGeometryFunctions(chartData) {
    chartData.msxChartGeometry = {};
    var msxCG = chartData.msxChartGeometry;

    msxCG.canvasHeight                 = undefined;
    msxCG.canvasWidth                  = undefined;
    msxCG.scalingFactor                = undefined;
    msxCG.widthAvailableForGroup       = undefined;
    msxCG.groupWidthMargin             = undefined;
    msxCG.widthAvailableForRewardBars  = undefined;
    msxCG.widthAvailableForRewardBar   = undefined;
    msxCG.rewardSpacerWidth            = undefined;
    msxCG.rewardBarWidth               = undefined;
    msxCG.xAxisOriginX                 = undefined;
    msxCG.xAxisOriginY                 = undefined;
    msxCG.xAxisLength                  = undefined;
    msxCG.yAxisOriginX                 = undefined;
    msxCG.yAxisOriginY                 = undefined;
    msxCG.yAxisLength                  = undefined;
    msxCG.actionLinesOriginX           = [];
    msxCG.actionLinesOriginY           = undefined;
    msxCG.actionLineLength             = undefined;
    msxCG.positiveLineOriginY          = [];
    msxCG.positiveLineLength           = undefined;
    msxCG.positiveLineOriginX          = undefined;
    msxCG.positiveMarkerValues         = [];
    msxCG.positiveMarkerYPixelsFromXAxis   = [];


    msxCG.initChartDimensions = function (canvasHeight, canvasWidth, groupWidthMarginFactor, rewardSpacerWidth) {
        msxCG.canvasHeight = canvasHeight;
        msxCG.canvasWidth = canvasWidth;
        msxCG.widthAvailableForGroup = Math.floor(msxCG.canvasWidth / 2);
        msxCG.groupWidthMargin = Math.floor((msxCG.widthAvailableForGroup * groupWidthMarginFactor) / 2);
        msxCG.widthAvailableForRewardBars = Math.floor(msxCG.widthAvailableForGroup - (3 * msxCG.groupWidthMargin));
        msxCG.widthAvailableForRewardBar = Math.floor(msxCG.widthAvailableForRewardBars / chartData.rewardNames.length);
        msxCG.rewardBarWidth = Math.floor(msxCG.widthAvailableForRewardBar - (rewardSpacerWidth));
        //biggest bar should take up .75 of canvasHeight/2  (120 * scalingFactor == 3/4 * canvasHeight/2) (we assumed scalingFactor == 2)
        msxCG.scalingFactor = ( ((msxCG.canvasHeight / 2) * 0.75) / chartData.getMaxAbsoluteValueReward() ).toFixed(2);
    }

    msxCG.positionRewardBar = function (maxValueAction, rewardBar, rewardIndex) {
            //bar.originX = (groupWidthMargin*2) + j *(rewardBarWidth) **For picked best action**
            //bar.originX = widthAvailableForGroup + (groupWidthMargin*2) + j *(rewardBarWidth) **For all other actions**
            //bar.originY = canvasHeight/2 ==> constant 320.0
            
            if (maxValueAction == true) {
                rewardBar.msxChartGeometry.originX = Math.floor((msxCG.groupWidthMargin * 2) + (rewardIndex * msxCG.rewardBarWidth));
            } else {//BUG?? is this right v
                rewardBar.msxChartGeometry.originX = Math.floor(msxCG.widthAvailableForGroup + msxCG.groupWidthMargin + (rewardIndex * msxCG.rewardBarWidth));
            }
            // console.log("rewardindex                  " + rewardIndex);
            // console.log("msxCG.groupWidthMargin       " + msxCG.groupWidthMargin);
            // console.log("msxCG.rewardBarWidth         " + msxCG.rewardBarWidth);
            // console.log("msxCG.widthAvailableForGroup " + msxCG.widthAvailableForGroup);
            // console.log("msxCG.groupWidthMargin       " + msxCG.groupWidthMargin);
            // console.log("rewardBar.msxChartGeometry.originX " + rewardBar.msxChartGeometry.originX);
            rewardBar.msxChartGeometry.originY = msxCG.canvasHeight / 2;
        }

        
    msxCG.getActionBarNameForCoordinatesForAction = function(x,y,action){
        var result = "None";
        for (var i in action.bars){
            var bar = action.bars[i];
            var isHeightNegative = true;
            if (bar.value > 0){
                isHeightNegative = false;
            }
            var barCg = bar.msxChartGeometry;
            if (barCg != undefined) {
                if (chartData.isPointInsideBox(x, y, barCg.originX, barCg.originY, barCg.width, barCg.height, isHeightNegative)){ 
                    result = bar.fullName;
                } 
            }
        }
        return result;
    }
    msxCG.getActionBarNameForCoordinates = function(x,y, winningAction,losingAction) {
        var result = msxCG.getActionBarNameForCoordinatesForAction(x,y,losingAction);
        if (result == "None"){
            result = msxCG.getActionBarNameForCoordinatesForAction(x,y,winningAction);
        }
        return result;
    }
    msxCG.dimensionRewardBar = function (rewardBar) {
        rewardBar.msxChartGeometry.scaledValue = rewardBar.value * msxCG.scalingFactor;
        //ch.actionRewardForNameMap["action_0.reward_0"]
        //widthAvailableForRewardBars = widthAvailableForGroup - 2 * groupWidthMargin
        //widthAvailableForRewardBar = widthAvailableForRewardBars / rewardBarCount
        rewardBar.msxChartGeometry.height = Math.abs(rewardBar.msxChartGeometry.scaledValue);
        rewardBar.msxChartGeometry.width = msxCG.rewardBarWidth;
    }
    
    msxCG.positionActionLabels = function(minDistanceFromBarOrAxis) {
        var maxAbsValNegBar = chartData.getMaxAbsValNegativeReward();
        var actionLabelY = undefined;
        if (maxAbsValNegBar == undefined){
            actionLabelY = msxCG.canvasHeight / 2 + minDistanceFromBarOrAxis;
        }
        else if (maxAbsValNegBar < minDistanceFromBarOrAxis){
            actionLabelY = msxCG.canvasHeight / 2 + minDistanceFromBarOrAxis;
        }
        else {
            actionLabelY = msxCG.canvasHeight / 2 + maxAbsValNegBar * msxCG.scalingFactor + minDistanceFromBarOrAxis;
        }
        for (var i in chartData.actions){
            var action = chartData.actions[i];
            //X = (groupWidthMargin*2) + (widthAvailableForGroup / 2) **For picked best action**
            //X = widthAvailableForGroup + (groupWidthMargin*2) + (widthAvailableForGroup / 2) **For all other actions**
            var centerXOfLabel;
            if (action.msxMaxValueAction) {
                //action.msxChartGeometry.actionLabelOriginX = (msxCG.groupWidthMargin*2) + (msxCG.widthAvailableForGroup / 2);
                centerXOfLabel = Math.floor(msxCG.groupWidthMargin*2 + msxCG.widthAvailableForRewardBars / 2);
                
            } else {
                //action.msxChartGeometry.actionLabelOriginX = msxCG.widthAvailableForGroup + (msxCG.groupWidthMargin*2) + (msxCG.widthAvailableForGroup / 2); 
                centerXOfLabel = Math.floor(msxCG.widthAvailableForGroup + msxCG.groupWidthMargin + msxCG.widthAvailableForRewardBars / 2);
            }
            action.msxChartGeometry.actionLabelOriginX = centerXOfLabel - 35;
            action.msxChartGeometry.actionLabelOriginY = actionLabelY;
        }
    }
    msxCG.positionValueMarkers = function (numberOfLines) {
        msxCG.positiveMarkerValues = [numberOfLines];
        msxCG.positiveMarkerYPixelsFromXAxis = [numberOfLines];
        var valueMarkers = Math.floor(chartData.getMaxAbsoluteValueReward() / numberOfLines);
        var setValue = valueMarkers;
        for (var i=0; i < numberOfLines; i++) {
            msxCG.positiveMarkerValues[i] = setValue;
            msxCG.positiveMarkerYPixelsFromXAxis[i] = (setValue * msxCG.scalingFactor).toFixed(2);
            setValue += valueMarkers;
        }
    }
    msxCG.positionValueLines = function (numberOfLines) {
        msxCG.positiveLine = [numberOfLines];
        var lineSpacing = Math.floor(chartData.getMaxAbsoluteValueReward() / numberOfLines * msxCG.scalingFactor);
        msxCG.positiveLineLength = msxCG.canvasWidth - 2 * msxCG.groupWidthMargin;
        msxCG.positiveLineOriginX = msxCG.groupWidthMargin;
        for (var i = 0; i < numberOfLines; i++) {
            msxCG.positiveLine[i] = {};
            msxCG.positiveLineOriginY[i] = ((msxCG.canvasHeight / 2) + (1 + Number(i)) * lineSpacing).toFixed(2);
        }
    }

    msxCG.positionPairedTooltips = function(action1, action2){
        for (var i in action1.bars) {
            var bar1 = action1.bars[i];
            var bar2 = action2.bars[i];
            bar1.msxChartGeometry.scalingFactor = msxCG.scalingFactor;
            bar2.msxChartGeometry.scalingFactor = msxCG.scalingFactor;

            // tooltip origin is the tip of each arrow; each bar will own it's own tooltip which will be directly overlaid on it's pair reward bar's tooltip
            bar1.msxChartGeometry.tooltipPairOriginX1 = bar1.msxChartGeometry.originX + msxCG.rewardBarWidth / 2;
            bar1.msxChartGeometry.tooltipPairOriginX2 = bar2.msxChartGeometry.originX + msxCG.rewardBarWidth / 2;
            
            bar2.msxChartGeometry.tooltipPairOriginX1 = bar1.msxChartGeometry.originX + msxCG.rewardBarWidth / 2;
            bar2.msxChartGeometry.tooltipPairOriginX2 = bar2.msxChartGeometry.originX + msxCG.rewardBarWidth / 2;
                
            var distanceAboveXAxisBar1 = 0;
            //
            // each bar needs to remember both its and its counterpart's value's sign
            // because both bars need to create an identical tooltip that touches both bars
            // and thus we need to know at tooltip-drawing time how to position the arrows for both
            // so that the arrow doesn't cover over the value tooltips for the bars
            //
            if (bar1.value > 0){
                distanceAboveXAxisBar1 = bar1.value * msxCG.scalingFactor;
                bar1.msxChartGeometry.leftBarIsPositive = true;
                bar2.msxChartGeometry.leftBarIsPositive = true;
            }
            else {
                bar1.msxChartGeometry.leftBarIsPositive = false;
                bar2.msxChartGeometry.leftBarIsPositive = false;
            }
            var distanceAboveXAxisBar2 = 0;
            if (bar2.value > 0){
                distanceAboveXAxisBar2 = bar2.value * msxCG.scalingFactor;
                bar1.msxChartGeometry.rightBarIsPositive = true;
                bar2.msxChartGeometry.rightBarIsPositive = true;
            }
            else {
                bar1.msxChartGeometry.rightBarIsPositive = false;
                bar2.msxChartGeometry.rightBarIsPositive = false;
            }
            bar1.msxChartGeometry.tooltipPairOriginY1 = msxCG.canvasHeight/2 - distanceAboveXAxisBar1;
            bar1.msxChartGeometry.tooltipPairOriginY2 = msxCG.canvasHeight/2 - distanceAboveXAxisBar2;
           
            bar2.msxChartGeometry.tooltipPairOriginY1 = msxCG.canvasHeight/2 - distanceAboveXAxisBar1;
            bar2.msxChartGeometry.tooltipPairOriginY2 = msxCG.canvasHeight/2 - distanceAboveXAxisBar2;
        }
    }
    msxCG.positionTooltips = function(action, actionPositionInGraph) {
        var barsPerAction = action.bars.length;
        //if (action.msxMaxValueAction == false) {
        for (var j in action.bars) {
            var bar = action.bars[j];
            var calc = Number((Number(actionPositionInGraph) * Number(barsPerAction)) + Number(j));
            bar.msxChartGeometry.tooltipOriginX = bar.msxChartGeometry.originX + msxCG.rewardBarWidth;
            bar.msxChartGeometry.tooltipOriginY = msxCG.canvasHeight/2 - bar.msxChartGeometry.scaledValue * 0.75;
        }
    }

    msxCG.positionValueTooltips = function(action) {
        for (var i in action.bars){
            var rewardBar = action.bars[i];
            rewardBar.msxChartGeometry.tooltipOriginX = rewardBar.msxChartGeometry.originX - Number(msxCG.rewardBarWidth / 2);
            // (canvasHeight / 2) - ((ch.rewardBar[i].bars[j].value * scalingFactor) * 0.75)
            if (rewardBar.value >= 0) {
                rewardBar.msxChartGeometry.tooltipOriginY = msxCG.canvasHeight/2 - rewardBar.msxChartGeometry.scaledValue - 20;
            } else {
                rewardBar.msxChartGeometry.tooltipOriginY = msxCG.canvasHeight/2 - rewardBar.msxChartGeometry.scaledValue;
            }
        }
    }

    msxCG.positionXAxisLine = function(){
        // xAxisLength = width - 2 * groupWidthMargin
        // xAxisOriginX = groupWidthMargin;
        // xAxisOriginY = height / 2
        msxCG.xAxisLength = msxCG.canvasWidth - 2 * msxCG.groupWidthMargin;
        msxCG.xAxisOriginY = msxCG.canvasHeight / 2;
        msxCG.xAxisOriginX = msxCG.groupWidthMargin;
    }

    msxCG.positionYAxisLine = function(){
        // yAxisLength = maxAbsRewardValue * 2 * scalingFactor
        // yAxisOriginX = groupWidthMargin;
        // yAxisOriginY = (canvasHeight - yAxisLength) / 2
        msxCG.yAxisLength = chartData.getMaxAbsoluteValueReward() * 2 * msxCG.scalingFactor;
        msxCG.yAxisOriginY = (msxCG.canvasHeight - msxCG.yAxisLength) / 2;
        msxCG.yAxisOriginX = msxCG.groupWidthMargin;
    }

    msxCG.positionActionSeparatorLines = function() {
        // acitonLinesLength = maxAbsRewardValue * 2 * scalingFactor + aBitMore
        // actionLinesOriginX
        // actionLinesOriginY = (canvasHeight - yAxisLength) / 2
        msxCG.actionLinesLength = Math.floor(chartData.getMaxAbsoluteValueReward() * 2 * msxCG.scalingFactor);
        var actionLineBasedOffYAxis = chartData.getMaxAbsoluteValueReward() * 2 * msxCG.scalingFactor;
        msxCG.actionLinesOriginY = (msxCG.canvasHeight - actionLineBasedOffYAxis) / 2;
        msxCG.actionLinesOriginX.push(msxCG.canvasWidth / 2);
    }

    return chartData;
}